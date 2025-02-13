from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from libs.logger.init_logger import logger

driver: webdriver.Chrome = None

BASE_URL = "https://www.freelancermap.com/"


def get_driver(url: str = BASE_URL) -> webdriver.Chrome:
    global driver
    if driver is not None:
        return driver
    # Set up the Chrome WebDriver
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )
    # Open the webpage with full window
    driver.maximize_window()
    driver.get(url)
    return driver


def navigate_to(url: str):
    global driver
    if driver is None:
        driver = get_driver()
    driver.get(url)
    return driver


def close_driver():
    global driver
    if driver is not None:
        driver.quit()
        driver = None
