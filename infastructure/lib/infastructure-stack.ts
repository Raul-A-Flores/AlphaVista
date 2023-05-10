import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as lambda from 'aws-cdk-lib/aws-lambda';
import * as apiGateway from "aws-cdk-lib/aws-apigateway"
import * as dotenv from "dotenv"

dotenv.config()

export class InfastructureStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'InfastructureQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });

    // aws base layer 
    const layer = new lambda.LayerVersion(this, "BaseLayer", {
      code: lambda.Code.fromAsset("lambda_base_layer/layer.zip"),
      compatibleRuntimes: [lambda.Runtime.PYTHON_3_9],
    });


    const apiLambda = new lambda.Function(this, "ApiFunction",{
      runtime: lambda.Runtime.PYTHON_3_9,
      code: lambda.Code.fromAsset("../app/"),
      handler: "saas_api.handler",
      layers: [layer],
      environment:{
        OPENAI_API_KEY: process.env.OPENAI_API_KEY ?? "",
      },
    });

    // lambda integration

    const saasApi = new apiGateway.RestApi(this, "RestApi",{
      restApiName: "Saas main API",
    });

   /*  const lambdaApiIntegration = new apiGateway.LambdaIntegration(apiLambda);
    saasApi.root.addProxy({
      defaultIntegration: lambdaApiIntegration
    }) */

    saasApi.root.addProxy({
      defaultIntegration: new apiGateway.LambdaIntegration(apiLambda)
    })
  }
}
