import allure
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from pages.staging_app_hord import StagingAppHord
from utils.javascript_executors import scroll_element_into_view


@allure.feature('Sidebar open by default')
@allure.story('Check if sidebar open by default on Hord page')
@pytest.mark.usefixtures("driver")
def test_sidebar_open_after_page_load(driver: WebDriver) -> None:
    """
    Test sidebar open by default on Hord page
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    with (allure.step('Verify that sidebar open by default on Hord page')):
        assert not staging_app_hord.is_sidebar_collapsed, "Sidebar should not be collapsed initially"


@allure.feature('Sidebar collapsed')
@allure.story('Check if sidebar collapsed by toggle button')
@pytest.mark.usefixtures("driver")
def test_sidebar_collapsed(driver: WebDriver) -> None:
    """
    Test sidebar collapsed on Hord page
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    staging_app_hord.click_toggle_button_with_js()

    with (allure.step('Verify that sidebar collapsed by toggle button')):
        assert staging_app_hord.is_sidebar_collapsed, "Sidebar should be collapsed after toggle button click"


@allure.feature('Sidebar opened')
@allure.story('Check if sidebar opened by toggle button')
@pytest.mark.usefixtures("driver")
def test_sidebar_open(driver: WebDriver) -> None:
    """
    Test sidebar open on Hord page by toggle button
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    staging_app_hord.click_toggle_button_with_js()
    staging_app_hord.click_toggle_button_with_js()
    with (allure.step('Verify that sidebar open by toggle button')):
        assert not staging_app_hord.is_sidebar_collapsed, "Sidebar should not be collapsed after toggle button click"


@allure.feature('FAQ section exists')
@allure.story('Check if FAQ section exists on page')
@pytest.mark.usefixtures("driver")
def test_faq_section_exists(driver: WebDriver) -> None:
    """
    Test FAQ section exists on page
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    with (allure.step('Verify that FAQ section exists on page')):
        assert staging_app_hord.is_faq_section_exists(), "FAQ section should exist on page"


@allure.feature('FAQ ETH question exists')
@allure.story('Check if FAQ ETH question exists on page')
@pytest.mark.usefixtures("driver")
def test_faq_eth_question_exists(driver: WebDriver) -> None:
    """
    Test FAQ ETH question exists on page
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    with (allure.step('Verify that FAQ ETH question exists on page')):
        assert staging_app_hord.is_faq_eth_exists(), "FAQ ETH question should exist on page"


@allure.feature('FAQ ETH answer exists')
@allure.story('Check if FAQ ETH answer exists on page')
@pytest.mark.usefixtures("driver")
def test_faq_eth_answer_exists(driver: WebDriver) -> None:
    """
    Test FAQ ETH answer exists on page
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    with (allure.step('Verify that FAQ ETH answer exists on page')):
        assert staging_app_hord.is_faq_eth_answer_exists(), "FAQ ETH answer should exist on page"



@allure.feature('FAQ ETH question open')
@allure.story('Check if FAQ ETH question can be open')
@pytest.mark.usefixtures("driver")
def test_faq_eth_question_open(driver: WebDriver) -> None:
    """
    Test FAQ ETH question can be open
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    scroll_element_into_view(driver, staging_app_hord.pointer_faq_eth)
    staging_app_hord.toggle_faq_eth_question()
    with (allure.step('Verify that FAQ ETH question can be open')):
        assert staging_app_hord.is_faq_eth_question_open(), "FAQ ETH question should be open after toggle button click"


@allure.feature('FAQ ETH question open and close')
@allure.story('Check if FAQ ETH question can be open and close')
@pytest.mark.usefixtures("driver")
def test_faq_eth_question_open_and_close(driver: WebDriver) -> None:
    """
    Test FAQ ETH question can be open and close
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    scroll_element_into_view(driver, staging_app_hord.pointer_faq_eth)
    staging_app_hord.toggle_faq_eth_question()
    staging_app_hord.toggle_faq_eth_question()
    with (allure.step('Verify that FAQ ETH question can be close')):
        assert not staging_app_hord.is_faq_eth_question_open(), "FAQ ETH question should be close after toggle button second click"


@allure.feature('FAQ ETH question stay open')
@allure.story('Check if FAQ ETH question stays open after second question open')
@pytest.mark.usefixtures("driver")
def test_faq_eth_question_stays_open(driver: WebDriver) -> None:
    """
    Test FAQ ETH question stays open after second question open
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    scroll_element_into_view(driver, staging_app_hord.pointer_faq_eth)
    staging_app_hord.toggle_faq_eth_question()
    staging_app_hord.click_faq_hord_answers_button_with_js()
    with (allure.step('Verify that FAQ ETH question stays open')):
        assert staging_app_hord.is_faq_eth_question_open(), "FAQ ETH question should be open after toggle button of another question clicked"


@allure.feature('Last Airdrops section exists')
@allure.story('Check if Last Airdrops section exists on Revenue Share')
@pytest.mark.usefixtures("driver")
def test_last_airdrop_section_exists(driver: WebDriver) -> None:
    """
    Test Last Airdrops section exists on Revenue Share
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    staging_app_hord.click_revenue_share_link()
    with (allure.step('Check if Last Airdrops section exists on Revenue Share')):
        assert staging_app_hord.is_last_airdrops_section_exists(), "Last Airdrops section should exist on Revenue Share"


@allure.feature('Last Airdrops Epoch List not empty')
@allure.story('Check if Last Airdrops Epoch List is not empty on Revenue Share')
@pytest.mark.usefixtures("driver")
def test_last_airdrop_epoch_containers_list_not_empty(driver: WebDriver) -> None:
    """
    Test Last Airdrops Epoch List is not empty on Revenue Share
    :param driver: WebDriver
    """
    staging_app_hord = StagingAppHord(driver)
    staging_app_hord.click_revenue_share_link_with_js()
    scroll_element_into_view(driver, staging_app_hord.last_airdrop_header)
    with (allure.step('Check if Last Airdrops Epoch List is not empty on Revenue Share on Revenue Share')):
        assert staging_app_hord.is_last_airdrop_epoch_containers_list_not_empty(), "Last Airdrops Epoch List is empty on Revenue Share"