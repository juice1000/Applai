import uvicorn
from fastapi import FastAPI

from libs.embed.embed_document import embed_document
from libs.generate.generate import generate_response

app = FastAPI()


@app.get("/embed/")
def embed_sources():
    embed_document()
    return {"message": "Document loaded"}


@app.post("/generate/")
def generate(req: dict):
    # generate the application from job description
    prompt = req["prompt"]
    response = generate_response(prompt)
    return {"message": response}


if __name__ == "__main__":
    # run the server
    uvicorn.run("main:app", reload=True)
