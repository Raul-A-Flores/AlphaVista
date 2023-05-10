from fastapi import FastAPI,HTTPException
from saas import generate_branding_snippit, generate_keywords
from mangum import Mangum


app = FastAPI()
handler = Mangum(app)
MAX_INPUT_LENGTH = 32

# Generating Snippit

@app.get("/generate_snippit")
async def generating_branding_api(prompt: str):
    validate_input_length(prompt)
    snippit = generate_branding_snippit(prompt)
    return {"Snippit": snippit, "Keywords": []}


# Generating Keywords
@app.get("/generate_keyword")
async def generating_keyword_api(prompt: str):
    validate_input_length(prompt)
    keyword = generate_keywords(prompt)
    return {"Snippit" : None, "Keywords": keyword}


@app.get("/generate_brand")
async def generating_keyword_api(prompt: str):
    validate_input_length(prompt)
    snippit = generate_branding_snippit(prompt)
    keyword = generate_keywords(prompt)
    return {"Snippit": snippit, "Keywords": keyword}

def validate_input_length(prompt:str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(status_code=404, detail=f"Input length is too long, must be under {MAX_INPUT_LENGTH}")

    pass


#uvicorn saas_api:app --reload