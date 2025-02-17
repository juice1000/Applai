import uvicorn
from custom_types import FieldRequest, JobStatusUpdate, PromptRequest
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from libs.db.db_operations import add_field_to_table, get_table_schema
from libs.db.get_job import get_all_jobs
from libs.db.init_db import initialize_db
from libs.db.write_job import update_job_by_id
from libs.embed.embed_document import embed_document
from libs.generate.retrieve_from_rag import retrieve_from_rag_experimental
from libs.llm.init_llm import init_llm_services
from libs.logger.init_logger import logger
from libs.scrape_and_drive.application_driver import apply_from_db
from libs.scrape_and_drive.scraper import scrape_jobs_fmap
from write_application import write_job_applications

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Hi from da server!"}


@app.get("/embed/")
def embed_sources(clear: bool = False):
    embed_document(clear=clear)
    return {"message": "Document loaded"}


@app.post("/prompt/")
def generate(req: PromptRequest):
    # generate the application from job description
    prompt = req.prompt
    response = retrieve_from_rag_experimental(prompt)
    return {"message": response}


@app.get("/write_applications/")
def write_applications(update: bool = False):
    print("Writing applications", update)
    # generate the application from job description
    number_of_jobs = write_job_applications(update=update)
    return {"message": f"Job applications generated for {number_of_jobs} jobs"}


# @app.get("/apply_from_files/")
# def apply_to_job():
#     # generate the application from job description
#     apply_from_files()


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


@app.put("/jobs/{job_id}")
def update_job_status(job_id: int, job_update: JobStatusUpdate):
    update_job_by_id(job_id, status=job_update.status)
    return {"message": f"Job {job_id} updated with status {job_update.status}"}


@app.get("/write_applications/{job_id}")
def write_single_job_application(job_id: int):
    print("Update application", job_id)
    # generate the application from job description
    number_of_jobs = write_job_applications(job_id=job_id)
    return {"message": f"Job applications generated for {number_of_jobs} jobs"}


@app.post("/db/")
def update_db_fields(req: FieldRequest):
    # add a field to the database table
    add_field_to_table(req.field_name, req.field_type)
    return {"message": "Field added to table"}


@app.get("/db/")
def get_db_schema():
    # get the database schema
    return get_table_schema()


if __name__ == "__main__":
    # Initialize services
    try:
        initialize_db()
        init_llm_services()
        uvicorn.run("main:app", reload=True)
    except RuntimeError as e:
        logger.error(str(e))
        exit(1)
