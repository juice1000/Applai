from libs.db.get_job import get_all_jobs, get_job_files, get_jobs_without_application
from libs.db.init_db import Job
from libs.db.write_job import update_job
from libs.generate.generate_application import generate_application
from libs.generate.retrieve_from_rag import retrieve_from_rag
from libs.logger.init_logger import logger
from libs.sanitize_input.text_to_json import text_to_json_string as ttj


def apply_from_files():
    logger.info("Applying from local job files...")
    # generate the application from job description
    job_files = get_job_files()
    for job in job_files:
        job_description = ttj(job)
        rag_retrieval_context = retrieve_from_rag(job_description)
        job = Job(
            title="Software Engineer",
            description=job_description,
            date_applied="2022-01-01",
            url="https://www.example.com",
            resume_context=rag_retrieval_context,
        )
        application_letter = generate_application(job)

        job.application_letter = application_letter
        # write_job(job)

    logger.info("Applications generated for provided files.")
    return {"message": "Job applications generated"}


def write_job_applications(update: bool = False):
    logger.info("Writing job applications to DB...")

    if not update:
        # retrieve all jobs without applications
        jobs = get_jobs_without_application()
    else:
        jobs = get_all_jobs()

    for job in jobs:
        # retrieve the context from the resume in regards to the job description
        rag_retrieval_context = retrieve_from_rag(job.description)
        job.resume_context = rag_retrieval_context

        # generate the application from job description
        application_letter = generate_application(job)
        job.application_letter = application_letter
        update_job(job)

    logger.info(
        "Applications generated and written to DB for jobs without applications."
    )
    return len(jobs)
