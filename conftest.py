import time
from typing import Generator, Optional, cast
import allure
import pytest
from _pytest.reports import TestReport
from _pytest.runner import CallInfo
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

from locators.locators import HordPageLocators
from utils.utils import wait_for_element


@pytest.fixture(scope="function")
def driver() -> WebDriver:
    """
    PyTest fixture to initialize a Chrome WebDriver instance with Selenium 4 options
    for hord base url
    :return: WebDriver instance
    """
    chrome_options = set_chrome_options()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://staging-app.hord.fi/")
    driver.maximize_window()
    assert wait_for_element(driver, HordPageLocators.SIDEBAR, timeout=15), "Sidebar element did not load in time"
    # WebDriverWait(driver, 15).until(lambda d: d.execute_script("return document.readyState") == "complete")
    yield driver
    driver.quit()


def set_chrome_options() -> Options:
    """
    create options for chromedriver instance
    :return: Options instance
    """
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    # chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.set_capability("goog:loggingPrefs", {"performance": "ALL"})
    return chrome_options


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item: pytest.Item, call: CallInfo) -> Generator[None, None, TestReport]:
    """
    PyTest hook to handle the result of each test and take a screenshot if a test fails.
    :param item: Test item currently executed
    :param call: Info about test call, like details of an exception
    :return: TestReport instance with test outcome
    """
    # Execute test, get outcome
    outcome = yield
    report: TestReport = outcome.get_result()

    # Take screenshot if a test fails, attach it to an Allure report
    # Before this check if the test is a function
    if report.when == 'call' and report.failed and isinstance(item, pytest.Function):
        driver: Optional[WebDriver] = cast(Optional[WebDriver], item.funcargs.get("driver", None))
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
