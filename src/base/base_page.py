import logging
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException 

from src.locators.base_locators.base_locators import BaseLocators
from src.pages.tp_pages.dashboard.tp_learners.tp_enquiries.tp_enquiries_page import TPDashboardLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # Fix the syntax error in logger initialization
        self.logger = logging.getLogger(self.__class__.__name__)

    def wait_and_click(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).click()
            self.logger.info(f"Clicked element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            raise

    def wait_and_type(self, locator, text, timeout=10):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()  # Clear existing text
            element.send_keys(text)
            self.logger.info(f"Entered '{text}' into element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not visible: {locator}")
            raise

    def get_title(self):
        title = self.driver.title
        self.logger.info(f"Retrieved page title: {title}")
        return title

    def get_url(self):
        url = self.driver.current_url
        self.logger.info(f"Retrieved current URL: {url}")
        return url

    def is_model_present(self, timeout=10):
        try:
            # Handle modal if present
            short_wait = WebDriverWait(self.driver, 2) 
            modal = short_wait.until(EC.visibility_of_element_located(TPDashboardLocators.MODAL))
            modal_btn = short_wait.until(EC.element_to_be_clickable(TPDashboardLocators.CLOSE_MODAL_BUTTON))
            if modal.is_displayed():
                self.driver.execute_script("arguments[0].click();", modal_btn)
                self.logger.info("\nModal was present. Closed it\n")
        except TimeoutException:
            self.logger.info("\nModal was not present") 
    
    
    def is_element_present(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f"Element get visible: {locator}")
        except TimeoutException:
            self.logger.error(f"Element was not present: {locator}")
            raise

    def get_visible_text(self, locator):
        elem = self.wait.until(EC.visibility_of_element_located(locator))
        text = elem.text.strip()
        self.logger.info(f"Text found for {locator}: '{text}'")
        return text
    
  