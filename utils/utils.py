from typing import Tuple
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_element_present(driver: WebDriver, locator: Tuple[By, str]) -> bool:
    """
    Generic function to check if an element is present on the page
    :param driver: WebDriver instance
    :param locator: Tuple containing the locator strategy
    :return: True if the element is present, False otherwise
    """
    try:
        driver.find_element(*locator)
        return True
    except NoSuchElementException:
        return False


def wait_for_element(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> bool:
    """
    Wait for element to be visible on the page
    :param driver: WebDriver instance
    :param locator: Tuple containing the locator strategy
    :param timeout: Maximum time to wait for the element to be visible, 10 sec by default
    :return: True if the element is visible, False otherwise
    """
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        return True
    except NoSuchElementException as e:
        print(f"Element {locator} not found on page within {timeout} seconds: {e}")
        return False


def wait_for_element_to_be_clickable(driver: WebDriver, locator: Tuple[By, str], timeout: int = 10) -> bool:
    """
        Wait for element to be clickable
        :param driver: WebDriver instance
        :param locator: Tuple containing the locator strategy
        :param timeout: Maximum time to wait for the element to be clickable, 10 sec by default
        :return: True if the element is visible, False otherwise
        """
    try:
        WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        return True
    except Exception as e:
        print(f"Element {locator} was not clickable during {timeout} seconds: {e}")

def hover_over_element(driver: WebDriver, locator: Tuple[By, str]) -> None:
    """
    Hover over an element on the page
    :param driver: WebDriver instance
    :param locator: Tuple containing the locator strategy
    """
    element: WebElement = driver.find_element(*locator)
    action = ActionChains(driver)
    action.move_to_element(element).perform()
