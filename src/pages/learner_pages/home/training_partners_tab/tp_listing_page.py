import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.locators.base_locators.base_locators import BaseLocators
from src.locators.learner_locators.home_page.course_detail_page.course_detail_page_locators import CourseDetailPageLocators
from src.locators.learner_locators.home_page.home_page_locators import HomePageLocators
from src.base.base_page import BasePage


class TPListingPage(BasePage):

    def select_and_open_specific_tp(self, tp_name):

        self.wait.until(EC.element_to_be_clickable(HomePageLocators.TRAINING_PARTNERS)).click()
        time.sleep(2)

        page_number = 1
        while True:
            self.wait.until(EC.visibility_of_all_elements_located(HomePageLocators.TP_CARDS))
            tp_titles = self.driver.find_elements(*HomePageLocators.TP_TITLE)

            for tp in tp_titles:
                if tp.is_displayed() and tp.text.strip() == tp_name.strip():
                    self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth',block:'center'});", tp)
                    self.driver.execute_script("arguments[0].click();", tp)
                    time.sleep(1)

                    try:
                        course_tab = self.wait.until(
                            EC.presence_of_element_located(CourseDetailPageLocators.COURSES_TAB)
                        )
                        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", course_tab)
                    except Exception:
                        return False
                    
                    try:
                        self.wait.until(EC.visibility_of_all_elements_located(CourseDetailPageLocators.TP_COURSES))
                        courses = [c for c in self.driver.find_elements(*CourseDetailPageLocators.TP_COURSES) if c.is_displayed()]
                        if not courses:
                            return False
                        
                        course = random.choice(courses)
                        self.driver.execute_script(
                            "window.scrollTo(0, arguments[0].getBoundingClientRect().top + window.pageYOffset - 100);",
                            course
                        )
                        self.wait.until(EC.element_to_be_clickable(course))
                        try:
                            course.click()
                        except:
                            self.driver.execute_script("arguments[0].click();", course)
                        return True

                    except:
                        return False

            # If TP not found on this page, click "Next"
            next_btns = self.driver.find_elements(*BaseLocators.NEXT_BTN)
            if not next_btns or next_btns[0].get_attribute("disabled"):
                break
            self.driver.execute_script("arguments[0].click();", next_btns[0])
            page_number += 1
            time.sleep(3)

        return False
