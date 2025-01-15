from libs.db.get_job import get_job_files
from libs.db.init_db import Job
from libs.db.write_job import write_or_update_job
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
