from base.base_page import BasePage
from locators.learner_locators.dashboard.learner_dashboard_locators import LearnerDashboardLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LearnerDashboardPage(BasePage):
 
  MENU_OPTION={
  "dashboard":{
    "locator":LearnerDashboardLocators.DASHBOARD,
    "verify_text":"It’s time to find next course for you. Let’s get to it!"
  },
  "mycourses":{
    "locator":LearnerDashboardLocators.MYCOURSES,
    "verify_text":"My Courses"
    },
  "profile":{ 
    "locator":LearnerDashboardLocators.PROFILE,
    "verify_text":"Profile"
      }
  #  ,
  # "assessment":{ 
  #  "locator":LearnerDashboardLocators.ASSESSMENT,
  #  "verify_text":""
  #  },
  # "jobs":{ 
  #  "locator":LearnerDashboardLocators.JOBS,
  #  "verify_text":""
  #  },
  # "settings":{ 
  #  "locator":LearnerDashboardLocators.SETTINGS,
  #  "verify_text":""
  #}
  }

  def click_menu_option(self,option_name):
    self.wait_and_click(self.MENU_OPTION[option_name]["locator"])

  def is_menu_option_page_loaded(self,option):
    expected_text=self.MENU_OPTION[option]["verify_text"]
    xpath=f"//p[normalize-space(text())='{expected_text}']"  #compare by '='

    return WebDriverWait(self.driver,10).until(
    EC.visibility_of_element_located((By.XPATH,xpath))
    )

  #Navigate to Home page   
  def navigate_to_home(self):
    try:
        self.wait_and_click(LearnerDashboardLocators.LOGO)
    except Exception:
        try:
            logo = self.driver.find_element(*LearnerDashboardLocators.LOGO)
            self.driver.execute_script("arguments[0].click();", logo)
        except Exception as e:
            print(f"Failed to click logo: {str(e)}")
            raise