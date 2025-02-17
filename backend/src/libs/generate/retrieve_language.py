from langdetect import detect
from libs.db.init_db import Job
from libs.logger.init_logger import logger


def retrieve_language(job: Job):
    logger.info(f"Retrieving language for job {job.title}...")
    # detect the language of the job description
    response_text = detect(job.description)
    return response_text
