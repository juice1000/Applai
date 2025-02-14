from datetime import datetime

from libs.db.get_job import get_jobs_with_pending_application
from libs.db.write_job import update_job
from libs.logger.init_logger import logger
from libs.scrape_and_drive.driver_utils import (
    accept_cookies,
    check_box,
    click_button,
    input_text,
    wait_for_element,
)
from libs.scrape_and_drive.init_scraper import close_driver, get_driver, navigate_to
from libs.scrape_and_drive.scraper import login
from selenium.webdriver.common.by import By


def apply_from_db():

    logger.info("Applying from DB...")
    # generate the application from job description
    jobs = get_jobs_with_pending_application()
    return
    driver = get_driver()
    login(driver)

    for job in jobs:
        try:
            accept_cookies()
            # Navigate to the job URL
            driver = navigate_to(job.url)
            # Get application form
            application_form = wait_for_element(
                driver, By.ID, "project-application-form"
            )
            # Insert application into the text field to apply to
            input_text(
                application_form,
                By.ID,
                "apply_project_form_content",
                job.application_letter,
            )
            # Click add resume button
            attachments = wait_for_element(driver, By.ID, "attachments")
            check_box(attachments, By.XPATH, '//*[@id="attachment-index-215084-1"]')
            # Submit the application
            click_button(application_form, By.XPATH, "//input[@type='submit']")

            logger.info(f"Applied to job: {job.title}")

            # Update the job status
            update_job(job, date_applied=datetime.now().strftime("%Y-%m-%d_%H:%M"))

        except Exception as e:
            logger.error(f"Failed to apply to job: {job.title}, error: {e}")

    close_driver()
    logger.info("Applications generated for jobs in DB.")
    return {"message": "Job applications generated"}
