from libs.db.get_job import (
    get_all_jobs_without_application,
    get_job_by_id,
    get_jobs_without_application_letter,
)
from libs.generate.workflow import init_application_workflow, run_workflow
from libs.logger.init_logger import logger
from libs.sanitize_input.text_to_json import text_to_json_string as ttj

chain = init_application_workflow()


def write_job_applications(update: bool = False, job_id: int = None):
    logger.info("Writing job applications to DB...")

    # look for a specific job by id
    if job_id:
        jobs = [get_job_by_id(job_id)]
    # get all jobs that haven't been applied to
    elif not update:
        # retrieve all jobs without application letter
        jobs = get_jobs_without_application_letter()
    else:
        # retrieve all jobs that haven't been applied to yet
        jobs = get_all_jobs_without_application()

    # generate applications for each job that was retrieved
    for job in jobs:
        run_workflow(job, chain)
        # update the job in the database

    logger.info(
        "Applications generated and written to DB for jobs without applications."
    )
    return len(jobs)
