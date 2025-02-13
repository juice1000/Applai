from datetime import datetime

import uvicorn
from fastapi import FastAPI

from apply import apply_from_files, write_job_applications
from custom_types import PromptRequest
from libs.db.get_job import get_all_jobs
from libs.db.init_db import initialize_db
from libs.db.write_job import update_job
from libs.embed.embed_document import embed_document
from libs.generate.retrieve_from_rag import retrieve_from_rag_experimental
from libs.logger.init_logger import logger
from libs.scrape_and_drive.application_driver import apply_from_db
from libs.scrape_and_drive.scraper import scrape_jobs_fmap

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hi from da server!"}


@app.get("/embed/")
def embed_sources():
    embed_document()
    return {"message": "Document loaded"}


@app.post("/prompt/")
def generate(req: PromptRequest):
    # generate the application from job description
    prompt = req.prompt
    response = retrieve_from_rag_experimental(prompt)
    return {"message": response}


@app.get("/write_applications/")
def write_applications(update: bool = False):
    # generate the application from job description
    number_of_jobs = write_job_applications(update)
    return {"message": f"Job applications generated for {number_of_jobs} jobs"}


@app.get("/apply_from_files/")
def apply_to_job():
    # generate the application from job description
    apply_from_files()


@app.get("/apply/")
def apply():
    # run scraper to apply from jobs that haven't been applied to
    apply_from_db()
    return {"message": "Job applications sent"}


@app.get("/scrape/")
def scrape_jobs():
    scrape_jobs_fmap()
    return {"message": "Job links scraped"}


@app.get("/jobs/")
def get_jobs():
    # generate the application from job description
    jobs = get_all_jobs()
    return jobs


if __name__ == "__main__":
    # run the server
    initialize_db()
    uvicorn.run("main:app", reload=True)
