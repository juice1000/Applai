import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

from libs.db.init_db import Job
from libs.db.write_job import write_or_update_job
from libs.logger.init_logger import logger
from libs.scrape_and_drive.driver_utils import (
    accept_cookies,
    check_box,
    click_button,
    input_text,
    wait_for_element,
    wait_for_page,
)
from libs.scrape_and_drive.init_scraper import close_driver, get_driver, navigate_to

# Loads the .env file
load_dotenv()

USER_EMAIL = os.getenv("USER_EMAIL")
USER_PASSWORD = os.getenv("USER_PASSWORD")
BASE_URL = "https://www.freelancermap.com/"


def login(driver: webdriver.Chrome):
    """
    Log in to freelancermap.com
    """

    driver.find_element(By.ID, "login-btn").click()
    login_form = wait_for_element(driver, By.CLASS_NAME, "login-form")
    input_text(login_form, By.NAME, "login", USER_EMAIL)
    input_text(login_form, By.NAME, "password", USER_PASSWORD)
    click_button(login_form, By.TAG_NAME, "button")
    wait_for_page()


def scrape_job_links():
    """
    Scrape job links from freelancermap.com using Selenium.

    Returns:
        list: A list of job links.
    """
    logger.info("Scraping job links from freelancermap.com...")

    try:
        driver = get_driver()
        # Navigate to the base URL
        accept_cookies()
        login(driver)

        # Navigate to projects page
        driver = navigate_to(BASE_URL + "it-projects.html")

        # Input job filter field
        job_filter_form = wait_for_element(driver, By.ID, "project-search-form")
        input_text(job_filter_form, By.TAG_NAME, "input", "python developer")
        click_button(job_filter_form, By.TAG_NAME, "button")

        filter_sidebar = wait_for_element(driver, By.CLASS_NAME, "filter-sidebar")

        check_box(filter_sidebar, By.XPATH, "//label[@for='remote-in-percent-remote']")
        check_box(filter_sidebar, By.XPATH, "//label[@for='excludeDachProjects']")
        check_box(
            filter_sidebar,
            By.XPATH,
            "//label[@for='search-option-hide-applied-projects']",
        )

        # Get job links
        jobs_links: list = driver.find_elements(By.CLASS_NAME, "project-title")

        logger.info(f"Found {len(jobs_links)} job links.")

        return [
            {"title": job.text, "link": job.get_attribute("href")} for job in jobs_links
        ]

    finally:
        # Close the WebDriver
        close_driver()


def scrape_job_details(job_link: dict[str, str]):
    """
    Scrape job description from a job link.

    Args:
        job_link (str): The job link.
    """
    logger.info(f"Scraping job details for {job_link['link']}...")

    try:
        job: Job = Job()
        job.title = job_link["title"]
        job.url = job_link["link"]

        # Navigate to the job link
        driver = get_driver()
        driver = navigate_to(job.url)

        # Accept cookies
        accept_cookies()

        # Get job details
        job_description = wait_for_element(driver, By.CLASS_NAME, "projectcontent")
        keywords = job_description.find_elements(By.CLASS_NAME, "keyword.no-truncate")
        content = wait_for_element(job_description, By.XPATH, '//*[@class="content"]')

        job.keywords = ", ".join([keyword.text for keyword in keywords])
        job.description = content.text

        logger.info("Job details scraped successfully.")

        return job

    finally:
        # Close the WebDriver
        close_driver()


def scrape_jobs_fmap():
    """
    Scrape job links and details from freelancermap.com.
    """
    logger.info("Starting scrape_jobs_fmap...")
    links = scrape_job_links()

    for idx, link in enumerate(links):
        job = scrape_job_details(link)
        write_or_update_job(job)
        logger.info(f"Scraped {idx} jobs out of {len(links)}.")
        idx += 1
