from libs.db.get_job import get_job_by_url
from libs.db.init_db import Job, engine
from libs.logger.init_logger import logger
from sqlmodel import Session


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
            logger.info("Existing job record updated.")
            return existing_job
        else:
            session.add(job)
            session.commit()
            logger.info("New job record saved.")
            return job


def update_job(job: Job):
    logger.info(f"Updating job {job.title} in DB with additional fields...")
    if not engine:
        raise Exception("No Engine for DB found")
    with Session(engine) as session:
        if job:
            session.merge(job)
            session.commit()
            logger.info("Job record updated.")
            return job
        else:
            logger.error(f"Job {job.id} not found")
            raise Exception(f"Job {job.id} not found")


def update_job_by_id(id: int, **kwargs):
    logger.info(f"Updating job {id} in DB with additional fields...")
    if not engine:
        raise Exception("No Engine for DB found")
    with Session(engine) as session:
        job = session.get(Job, id)
    if job:
        for key, value in kwargs.items():
            setattr(job, key, value)
        update_job(job=job)
    else:
        logger.error(f"Job {id} not found")
        raise Exception(f"Job {id} not found")
