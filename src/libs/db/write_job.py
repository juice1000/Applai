from sqlmodel import Session

from libs.db.init_db import Job, engine


def write_job(job: Job):
    if not engine:
        raise Exception("No Engine for DB found")
    with Session(engine) as session:
        session.add(job)
        session.commit()
        session.refresh(job)
        return job
