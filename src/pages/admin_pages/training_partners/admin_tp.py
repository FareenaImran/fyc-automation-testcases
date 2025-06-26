import re
import time
from selenium.webdriver.support import expected_conditions as EC
from src.base.base_page import BasePage
from src.locators.admin_locators.admin_base_locators import AdminBaseLocators
from src.locators.admin_locators.admin_dashboard.admin_dashboard_locators import AdminDashboardLocators
from src.locators.admin_locators.admin_tp.admin_tp_locators import AdminTPLocators
from selenium.webdriver.common.by import By
from src.locators.base_locators.base_locators import BaseLocators

class AdminTP(BasePage):

    TABS={
        "all_taps":{"locator":AdminTPLocators.AllTPSCount},
        "approved":{"locator":AdminTPLocators.APPROVED},
        "up_for_review":{"locator":AdminTPLocators.UP_FOR_REVIEW},
        "in_progress":{"locator":AdminTPLocators.INPROGRESS},
        "need_attention":{"locator":AdminTPLocators.NEEDS_ATTENTION},
        "unpublished":{"locator":AdminTPLocators.UNPUBLISHED}
    }

    def get_status_count(self,TABS):   
        self.is_element_present(TABS)
        self.wait_and_click(TABS)
        time.sleep(3)
        count_text = self.wait.until(
            EC.visibility_of_element_located(TABS)
        ).text.strip()

        if not count_text :
            raise AssertionError(f"Error getting 'All TPs' count: {count_text}")

        match = re.search(r'\((\d+)\)', count_text)
        if not match:
            raise AssertionError(f"Regex failed to match 'All TPs' count text: {count_text}")

        count = int(match.group(1))
        return count

    def get_no_of_rows_in_all_pages(self):
        
        total_rows=0
        page_number=1
        while True:
            time.sleep(3)
            rows=self.wait.until(EC.visibility_of_all_elements_located(BaseLocators.ROWS))
            all_rows_per_page=len(rows)
            self.logger.info(f"Page {page_number} : No of rows = {all_rows_per_page}")
            total_rows+=all_rows_per_page
            #Click on Next Button
            time.sleep(2)
            next_btn = self.driver.find_elements(*BaseLocators.NEXT_BTN)
            if not next_btn:
                self.logger.info("No Next button found — ending pagination.")
                break
            btn = next_btn[0]

            if btn.get_attribute("disabled"):
                self.logger.info("Next button is disabled — last page reached.")
                break

            self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth',block:'center'});",next_btn[0])
            self.driver.execute_script("arguments[0].click();",next_btn[0])
            
            page_number+=1

        self.logger.info(f"Total Rows Present in all Pages:{total_rows}")
        return total_rows

    def get_all_tps_count(self):
        self.is_element_present(AdminDashboardLocators.TP)
        self.wait_and_click(AdminDashboardLocators.TP)

        # Wait for the section containing the button to be visible (optional, but helps with async loads)
        # self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(.,'All TPs')]")))

        try:
            # Increase timeout for this specific wait if needed
            all_tps_button = self.wait.until(
                EC.visibility_of_element_located(AdminTPLocators.AllTPSCount)
            )
        except Exception as e:
            self.logger.error(f"Timeout waiting for All TPs button: {e}")
            raise AssertionError("Timeout waiting for All TPs button")

        all_tps_count_text = all_tps_button.text.strip()
        if not all_tps_count_text or 'All TPs (' not in all_tps_count_text:
            self.logger.error(f"Error getting 'All TPs' count: {all_tps_count_text}")
            raise AssertionError(f"Error getting 'All TPs' count: {all_tps_count_text}")

        match = re.search(r'\((\d+)\)', all_tps_count_text)
        if not match:
            self.logger.error(f"Regex failed to match 'All TPs' count text: {all_tps_count_text}")
            raise AssertionError(f"Regex failed to match 'All TPs' count text: {all_tps_count_text}")

        count = int(match.group(1))
        self.logger.info(f"Parsed All TPs count: {count}")
        return count





