from selenium.webdriver.common.by import By
class TPLearnerLocators:
    # More flexible locators
    ENQUIRIES_TAB = (By.XPATH, "//button[contains(.,'Enquiries')]")
    ENQUIRIES_TABLE = (By.XPATH, "//table[.//th[contains(.,'Message')]]")
    MSG_ROWS = (By.XPATH, "//table[.//th[contains(.,'Message')]]//tbody/tr")
    MSG_CELL = (By.TAG_NAME, "td")
