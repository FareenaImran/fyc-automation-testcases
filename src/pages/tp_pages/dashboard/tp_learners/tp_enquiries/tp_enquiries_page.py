import time
from src.locators.tp_locators.tp_dashboard.tp_dashboard_locators import TPDashboardLocators
from src.locators.tp_locators.tp_dashboard.tp_learner.tp_learner_locators import TPLearnerLocators
from src.base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class TPEnquiriesPage(BasePage):
    
    def get_latest_enquiry_msg_from_enquiries_table(self):
      try:
        self.wait_and_click(TPDashboardLocators.MENU_LEARNER)
        self.wait_and_click(TPLearnerLocators.ENQUIRIES_TAB)

        enquiry_rows=self.wait.until(EC.presence_of_all_elements_located(TPLearnerLocators.MSG_ROWS))
 
        if not enquiry_rows:
            raise AssertionError("No enquiries found")
 
        first_row=enquiry_rows[0]  #collect all td (values) of 1st row

        top_row_elements=first_row.find_elements(*TPLearnerLocators.MSG_CELL)

        if len(top_row_elements)<6:
            raise AssertionError("Table row dont have message rows")

        message_cell=top_row_elements[5]

        latest_msg=message_cell.text.strip()
        print(f"\nTop Message on TP Portal:\n{latest_msg}")

        return latest_msg

      except TimeoutException:
            print("Timed out waiting for enquiries table to load")
            raise
      except Exception as e:
            print(f"Error getting latest enquiry: {str(e)}")
            raise

