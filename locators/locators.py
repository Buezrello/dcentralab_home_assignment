from selenium.webdriver.common.by import By


class HordPageLocators:
    """
    Locators for Hord Page
    """
    FAQ_ETH_STAKING_XPATH: str = "//span[contains(text(),'What is ETH staking?')]"
    FAQ_HORD_REWARDS_XPATH: str = "//span[contains(text(),'What are HORD rewards?')]"
    FAQ_QUESTION_FOLLOWING_SIBLING_XPATH: str = "/following-sibling::div[@class='pointer']/div"

    SIDEBAR: tuple[By, str] = (By.XPATH, "//aside[contains(@class, 'duf-aside')]")
    TOGGLE_SIDEBAR_BUTTON: tuple[By, str] = (By.XPATH, "//aside[contains(@class, 'duf-aside')]/div/div/div/div/div/div[contains(@class, 'side-bar-toggler')]")
    FAQ_SECTION_HEADER: tuple[By, str] = (By.XPATH, "//h2[contains(text(),'Frequently Asked Questions')]")
    FAQ_ETH_STAKING: tuple[By, str] = (By.XPATH, FAQ_ETH_STAKING_XPATH)
    POINTER_FAQ_ETH_STAKING: tuple[By, str] = (By.XPATH, FAQ_ETH_STAKING_XPATH + FAQ_QUESTION_FOLLOWING_SIBLING_XPATH)
    POINTER_FAQ_HORD_REWARDS: tuple[By, str] = (By.XPATH, FAQ_HORD_REWARDS_XPATH + FAQ_QUESTION_FOLLOWING_SIBLING_XPATH)
    FAQ_ETH_STAKING_ANSWER: tuple[By, str] = (By.XPATH, "//*[contains(text(),'ETH staking is a process in which ETH holders can use their ETH to power the Ethereum blockchain and earn rewards in the process.')]")
    REVENUE_SHARE_LINK: tuple[By, str] = (By.XPATH, "//a[@href='/revenue-share']")
    REVENUE_SHARE_HEADER: tuple[By, str] = (By.XPATH, "//h2[contains(text(), 'Revenue Share')]")
    LAST_AIRDROPS_HEADER: tuple[By, str] = (By.XPATH, "//h2[contains(text(), 'Last Airdrops')]")
    LAST_AIRDROPS_EPOCH: tuple[By, str] = (By.XPATH, "//*[contains(@class, 'revenue-share-history-wrapper')]/div[contains(@class, 'epoch-conainer')]")