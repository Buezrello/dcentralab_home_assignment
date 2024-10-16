"""
POM Hord Page
"""
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from conftest import driver
from locators.locators import HordPageLocators
from utils.javascript_executors import click_element_with_js
from utils.utils import wait_for_element_to_be_clickable, hover_over_element, is_element_present, wait_for_element


class StagingAppHord:
    def __init__(self, driver: WebDriver) -> None:
        self.driver: WebDriver = driver


    def open(self, url: str) -> None:
        """
        Open the page by visiting the provided URL
        :param url: URL to ope
        """
        self.driver.get(url)

    @property
    def sidebar(self) -> WebElement:
        """
        Provide the sidebar element
        :return: Sidebar element
        """
        return self.driver.find_element(*HordPageLocators.SIDEBAR)

    @property
    def toggle_button(self) -> WebElement:
        """
        Provide the toggle sidebar button element
        :return: Toggle sidebar button element
        """
        return self.driver.find_element(*HordPageLocators.TOGGLE_SIDEBAR_BUTTON)

    @property
    def faq_section_header(self) -> WebElement:
        """
        Provide the faq section header element
        :return: Faq secrion header element
        """
        return self.driver.find_element(*HordPageLocators.FAQ_SECTION_HEADER)

    @property
    def faq_eth(self) -> WebElement:
        """
        Provide the faq eth element
        :return: Faq eth element
        """
        return self.driver.find_element(*HordPageLocators.FAQ_ETH_STAKING)

    @property
    def pointer_faq_eth(self) -> WebElement:
        """
        Provide the toggle button for faq eth question
        :return: Toggle button for faq eth question
        """
        return self.driver.find_element(*HordPageLocators.POINTER_FAQ_ETH_STAKING)

    @property
    def pointer_faq_hord(self) -> WebElement:
        """
        Provide the toggle button for faq hord reward question
        :return: Toggle button for faq hord reward question
        """
        return self.driver.find_element(*HordPageLocators.POINTER_FAQ_HORD_REWARDS)

    @property
    def revenue_share_link(self) -> WebElement:
        """
        Provide the revenue share link
        :return: Link to revenue share
        """
        return self.driver.find_element(*HordPageLocators.REVENUE_SHARE_LINK)

    @property
    def last_airdrop_epoch_containers(self) -> list:
        """
        Provide list of last airdrop epoch containers
        :return: List of last airdrop epoch containers
        """
        return self.driver.find_elements(*HordPageLocators.LAST_AIRDROPS_EPOCH)

    @property
    def last_airdrop_header(self) -> WebElement:
        """
        Provide last airdrop header element
        :return: Last airdrop header element
        """
        return self.driver.find_element(*HordPageLocators.LAST_AIRDROPS_HEADER)

    def wait_for_toggle_button_to_be_clickable(self) -> bool:
        """
        Wait for toggle button to be clickable
        :return: True or False
        """
        return wait_for_element_to_be_clickable(self.driver, HordPageLocators.TOGGLE_SIDEBAR_BUTTON, timeout=15)

    def hover_over_toggle_sidebur_button(self) -> None:
        """
        Hover over toggle button
        """
        hover_over_element(self.driver, HordPageLocators.TOGGLE_SIDEBAR_BUTTON)

    def toggle_sidebar(self) -> None:
        """
        Collapse / Open sidebar by clicking button on the sidebar
        """
        self.hover_over_toggle_sidebur_button()
        if self.wait_for_toggle_button_to_be_clickable():
            self.toggle_button.click()
        else:
            raise Exception("Toggle sidebar button not clickable")

    def toggle_faq_eth_question(self) -> None:
        """
        Open / Close faq eth question by clicking button on the question
        :return:
        """
        if wait_for_element_to_be_clickable(self.driver, HordPageLocators.POINTER_FAQ_ETH_STAKING, timeout=15):
            self.pointer_faq_eth.click()
        else:
            raise Exception("Toggle faq eth question not clickable")

    def toggle_faq_hord_reward_question(self) -> None:
        """
        Open / Close faq hord reward question by clicking button on the question
        """
        if wait_for_element_to_be_clickable(self.driver, HordPageLocators.POINTER_FAQ_HORD_REWARDS, timeout=15):
            self.pointer_faq_hord.click()
        else:
            raise Exception("Toggle faq hord reward question not clickable")


    def click_toggle_button_with_js(self) -> None:
        """
        Click toggle sidebar button using JS
        """
        click_element_with_js(self.driver, self.toggle_button)

    def click_faq_hord_answers_button_with_js(self) -> None:
        """
        Click faq hord answers button using JS
        """
        click_element_with_js(self.driver, self.pointer_faq_hord)


    def click_revenue_share_link(self) -> None:
        """
        Open revenue share link by clicking button on the link
        """
        if wait_for_element_to_be_clickable(self.driver, HordPageLocators.REVENUE_SHARE_LINK, timeout=15):
            self.revenue_share_link.click()
        else:
            raise Exception("Revenue share link not clickable")
        wait_for_element(self.driver, HordPageLocators.REVENUE_SHARE_HEADER, timeout=15)

    def click_revenue_share_link_with_js(self) -> None:
        """
        Click revenue_share_link using JS
        """
        click_element_with_js(self.driver, self.revenue_share_link)
        wait_for_element(self.driver, HordPageLocators.REVENUE_SHARE_HEADER, timeout=15)

    @property
    def is_sidebar_collapsed(self) -> bool:
        """
        Check if the sidebar is collapsed by inspecting the class attribute
        :return: True if the sidebar is collapsed, False otherwise
        """
        sidebar_class: str = self.sidebar.get_attribute("class")
        return "sidebar-expanded" not in sidebar_class

    def is_faq_section_exists(self) -> bool:
        """
        Check if the faq section exists
        :return: True if the faq section exists, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.FAQ_SECTION_HEADER)

    def is_faq_eth_exists(self) -> bool:
        """
        Check if the faq eth question exists
        :return: True if the faq eth question exists, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.FAQ_ETH_STAKING)

    def is_faq_eth_answer_exists(self) -> bool:
        """
        Check if the faq eth answer exists
        :return: True if the faq eth answer exists, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.FAQ_ETH_STAKING_ANSWER)

    def is_faq_eth_question_open(self) -> bool:
        """
        Check if the faq eth question open
        :return: True if the faq eth question open, False otherwise
        """
        faq_eth_question_class: str = self.pointer_faq_eth.get_attribute("class")
        return "toggled" in faq_eth_question_class

    def is_last_airdrops_section_exists(self) -> bool:
        """
        Check if the last airdrops section exists
        :return: True if the last airdrops section exists, False otherwise
        """
        return is_element_present(self.driver, HordPageLocators.LAST_AIRDROPS_HEADER)

    def is_last_airdrop_epoch_containers_list_not_empty(self) -> bool:
        """
        Check if the last airdrops epoch containers list not empty
        :return: True if the last airdrops epoch containers list not empty, False otherwise
        """
        if self.last_airdrop_epoch_containers:
            return True
        else:
            return False
