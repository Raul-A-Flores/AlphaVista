import os
import openai
import argparse


MAX_INPUT_LENGTH = 32


def main ():
    
    # print("Hello There")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str , required=True)
    
    args = parser.parse_args()
    user_input = args.input
    
    # print(f"User Input : {user_input}")
    generate_branding_snippit(user_input)
    
    if validate_length(user_input):
                
        
        result = generate_branding_snippit(user_input)
        keywords_result = generate_keywords(user_input)
        
        
        print(result)
        print(keywords_result)
    else:   
        raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted user input is {user_input} ")
        
    
def validate_length(prompt:str) -> bool:
    return len(prompt) <= MAX_INPUT_LENGTH 
    
    
# Snippit for our brand
def generate_branding_snippit(prompt: str) -> str:
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")


    enhanced_prompt = f"Generate upbeat branding snipping for {prompt}: "

    response = openai.Completion.create(model="text-davinci-003", prompt=enhanced_prompt, max_tokens=32)

    # print(response)
    
    #Extracting text from response
    branding_text = response["choices"][0]["text"]
    
    #Stripping White Space
    branding_text = branding_text.strip()
    
    #Adding ... to end of statement
    last_char = branding_text[-1]
    
    if last_char not in {".", "!", "?"}:
        branding_text += "..."
        
        
    #print(f"Snippit: {branding_text}")

    return branding_text



def generate_keywords(prompt: str) -> str:
    # Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")


    enhanced_prompt = f"Generate related popular branding tags to use on instagram and social media and add # for each keywords for {prompt}: "
    
    response = openai.Completion.create(model="text-davinci-003", prompt=enhanced_prompt, max_tokens=32)

    # print(response)
    
    #Extracting text from response 
    keywords_text = response["choices"][0]["text"]
    
    #Stripping White Space
    keywords_text = keywords_text.strip()
    
   
    #print(f"Tags: {keywords_text}")
    return keywords_text


if __name__ == "__main__":
    main()