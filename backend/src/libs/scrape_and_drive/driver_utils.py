import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from libs.scrape_and_drive.init_scraper import get_driver


def accept_cookies():
    # Accept cookies if button appears
    driver = get_driver()
    try:
        cookies_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        cookies_button.click()
        wait_for_page()
    except:
        pass


def wait_for_page(timeout=5):
    """
    Wait for the page to load by checking the document.readyState property.

    Args:
        timeout (int, optional): The maximum time to wait for the page to load. Defaults to 5.
    """
    driver = get_driver()
    end_time = time.time() + timeout

    while time.time() < end_time:
        if driver.execute_script("return document.readyState") == "complete":
            return
        time.sleep(0.1)
    raise TimeoutError("Timed out waiting for page to load")


def wait_for_element(
    root: WebElement | webdriver.Chrome,
    by: By,
    value: str,
    timeout=5,
) -> WebElement:
    """
    Wait for an element to be present in the DOM.

    Args:
        root (webdriver.Chrome or WebElement): The Chrome WebDriver instance.
        by (By): The locator strategy.
        value (str): The locator value.
        timeout (int, optional): The maximum time to wait for the element. Defaults to 5.
    """
    if isinstance(root, webdriver.Chrome):  # root is a WebDriver
        element = WebDriverWait(root, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    else:  # root is a WebElement
        element = root.find_element(by, value)

    if element.is_displayed():
        return element

    raise TimeoutError("Timed out waiting for element to load")


def input_text(
    root: WebElement | webdriver.Chrome,
    by: By,
    value: str,
    input: str,
):
    """
    Input text into a text field.

    Args:
        root (webdriver.Chrome | WebElement): The Chrome WebDriver instance or the parent element.
        element (WebElement): The text field element.
        text (str): The text to input.
    """
    element: WebElement = wait_for_element(root, by, value)
    scroll_to_view(root, element)
    element.send_keys(input)
    wait_for_page()


def scroll_top():
    """
    Scroll to the top of the page.
    """
    driver = get_driver()
    driver.execute_script("window.scrollTo(0, 0)")
    wait_for_page()


def scroll_and_click(root: WebElement | webdriver.Chrome, element: WebElement):
    """
    Scroll to an element.

    Args:
        root (webdriver.Chrome | WebElement): The Chrome WebDriver instance or the parent element.
        element (WebElement): The element to scroll to.
    """
    if isinstance(root, webdriver.Chrome):
        ActionChains(root).move_to_element(element).click().perform()
    else:
        root = get_driver()
        ActionChains(root).move_to_element(element).click().perform()
    wait_for_page()


def scroll_to_view(root: WebElement | webdriver.Chrome, element: WebElement):
    """
    Scroll to an element.

    Args:
        root (webdriver.Chrome | WebElement): The Chrome WebDriver instance or the parent element.
        element (WebElement): The element to scroll to.
    """
    if isinstance(root, webdriver.Chrome):
        ActionChains(root).move_to_element(element).perform()
    else:
        root = get_driver()
        ActionChains(root).move_to_element(element).perform()
    wait_for_page()


def click_button(
    root: WebElement | webdriver.Chrome,
    by: By,
    value: str,
):
    """
    Click a button.

    Args:
        root (webdriver.Chrome | WebElement): The Chrome WebDriver instance or the parent element.
        element (WebElement): The button element.
    """
    element: WebElement = wait_for_element(root, by, value)
    scroll_and_click(root, element)


def check_box(
    root: WebElement | webdriver.Chrome,
    by: By,
    value: str,
):
    """
    Click a button.

    Args:
        root (webdriver.Chrome | WebElement): The Chrome WebDriver instance or the parent element.
        element (WebElement): The button element.
    """

    element: WebElement = wait_for_element(root, by, value)

    # Scroll to the element and click it
    if isinstance(root, webdriver.Chrome):
        ActionChains(root).move_to_element(element).click().perform()
    else:
        root = get_driver()
        ActionChains(root).move_to_element(element).click().perform()

    # TODO: Not optimal, we should check if the checkbox is clickable rn or if the content has loaded after filter was applied
    time.sleep(4)
