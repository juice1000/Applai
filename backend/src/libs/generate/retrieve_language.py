from langdetect import detect
from libs.db.init_db import Job
from libs.logger.init_logger import logger


def retrieve_language(title: str, description: str) -> str:
    logger.info(f"Retrieving language for job {title}...")
    # detect the language of the job description
    response_text = detect(description)
    return response_text
