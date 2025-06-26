import time
import re
from locators.tp_locators.tp_dashboard.tp_dashboard_locators import TPDashboardLocators
from src.base.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.tp_locators.tp_dashboard.tp_courses.tp_courses_locators import TPCoursesLocators
from locators.tp_locators.tp_dashboard.tp_dashboard_locators import TPDashboardLocators
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class TPDashboardPage(BasePage):
  
  #Find button - Start Creating Course
  def is_start_creating_course_button_present(self):
        try:
           return self.driver.find_element(*TPCoursesLocators.START_CREATING_COURSE).is_displayed()
        except NoSuchElementException:
           return False

  #get count of Under Review & In Progress
  def get_course_count(self):
          self.is_model_present()
          try:    
              self.wait.until(EC.visibility_of_element_located(TPDashboardLocators.MENU_COURSE))
              self.wait_and_click(TPDashboardLocators.MENU_COURSE)
              self.wait.until(EC.visibility_of_element_located(TPCoursesLocators.IN_PROGRESS))
              self.wait.until(EC.visibility_of_element_located(TPCoursesLocators.UNDER_REVIEW))
              in_progress_btn=self.driver.find_element(*TPCoursesLocators.IN_PROGRESS)
              under_review_btn=self.driver.find_element(*TPCoursesLocators.UNDER_REVIEW)

              in_progress_match=int(re.search(r'\((\d+)\)',in_progress_btn.text).group(1))
              under_review_match=int(re.search(r'\((\d+)\)',under_review_btn.text).group(1))

              if in_progress_match or under_review_match:
                  return in_progress_match, under_review_match
              else:  
                  return 0,0
          
          except Exception as e:
              print(f"Failed to get course count:{str(e)}")
              return 0,0


  #Get TP Name
  def get_tp_name(self):
    tp_name_element=self.driver.find_element(*TPDashboardLocators.TP_USERNAME)
    tp_name=tp_name_element.text
    print(f"TP Name : {tp_name} ")
    return tp_name
  

  #Side Menu options
  MENU_OPTION={
    "dashboard":{
      "locator":TPDashboardLocators.MENU_DASHBOARD,
      "verify_text":"Welcome"
    },
    "profile":{
       "locator":TPDashboardLocators.MENU_PROFILE,
       "verify_text":"Your Profile"
    },
    "courses":{
      "locator":TPDashboardLocators.MENU_COURSE,
      "verify_text":"Courses"
    },
    "learner": {
      "locator":TPDashboardLocators.MENU_LEARNER,
      "verify_text":"Learners"
    },
    "settings":{
      "locator":TPDashboardLocators.MENU_SETTINGS,
      "verify_text":"Settings"
    }
  }

  def click_menu_option(self,option_name):
    self.wait_and_click(self.MENU_OPTION[option_name]["locator"])
  
  def is_menu_option_page_loaded(self, option):
    expected_text = self.MENU_OPTION[option]["verify_text"]
    xpath = f"//p[normalize-space(text())='{expected_text}']"
    return WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )

