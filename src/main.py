import uvicorn
from fastapi import FastAPI

from libs.db.init_db import Job, initialize_db
from libs.db.write_job import write_job
from libs.embed.embed_document import embed_document
from libs.generate.generate_application import generate_application
from libs.generate.retrieve_from_rag import (
    retrieve_from_rag,
    retrieve_from_rag_experimental,
)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hi from da server!"}


@app.get("/embed/")
def embed_sources():
    embed_document()
    return {"message": "Document loaded"}


@app.post("/retrieve/")
def generate(req: dict):
    # generate the application from job description
    prompt = req["prompt"]
    response = retrieve_from_rag_experimental(prompt)

    return {"message": response}


@app.post("/apply/")
def apply_to_job(req: dict):
    # generate the application from job description

    job_description = req["job_description"]
    rag_retrieval_context = retrieve_from_rag(job_description)
    print(rag_retrieval_context)
    # we write a fake job application in the DB
    job = Job(
        title="Software Engineer",
        description=job_description,
        date_applied="2022-01-01",
        url="https://www.example.com",
        resume_context=rag_retrieval_context,
    )
    application_letter = generate_application(job)
    print(application_letter)
    job.application_letter = application_letter
    write_job(job)
    return {"message": job.application_letter}


if __name__ == "__main__":
    # run the server
    initialize_db()
    uvicorn.run("main:app", reload=True)
