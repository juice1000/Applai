from sqlmodel import Session

from libs.db.get_job import get_job_by_url
from libs.db.init_db import Job, engine
from libs.logger.init_logger import logger


def write_or_update_job(job: Job):
    logger.info(f"Writing/updating job {job.url} in DB...")
    if not engine:
        raise Exception("No Engine for DB found")
    with Session(engine) as session:
        existing_job = get_job_by_url(job.url)
        if existing_job:
            # update the job details
            existing_job.title = job.title
            existing_job.description = job.description
            existing_job.keywords = job.keywords
            session.add(existing_job)
            session.commit()
            logger.info("Job record saved.")
            return existing_job
        else:
            session.add(job)
            session.commit()
            logger.info("Job record saved.")
            return job


def update_job(job: Job):
    logger.info(f"Writing job {job.title} to DB...")
    if not engine:
        raise Exception("No Engine for DB found")
    with Session(engine) as session:
        session.add(job)
        session.commit()
        logger.info("Job record saved.")
        return job
