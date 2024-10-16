import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


def scroll_element_into_view(driver: WebDriver, element: WebElement) -> None:
    """
    Scrolls the specified element into view using JavaScript execution
    :param driver: The WebDriver instance
    :param element: The WebElement instance to scroll into view
    :return: None
    """
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(0.5)

def click_element_with_js(driver: WebDriver, element: WebElement) -> None:
    """
    Click eledment using JS
    :param driver: WebDriver instance
    :param element: Element to click
    """
    driver.execute_script("arguments[0].click();", element)