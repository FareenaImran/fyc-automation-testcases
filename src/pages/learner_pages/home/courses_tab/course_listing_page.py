import random
import time

from locators.learner_locators.home_page.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from locators.learner_locators.dashboard.learner_dashboard_locators import LearnerDashboardLocators
class CourseListingPage(BasePage):
  
    sent_msg=None
    def select_and_open_random_course_card(self):
        try:
            try:
                self.wait.until(EC.element_to_be_clickable(LearnerDashboardLocators.LOGO)).click()
            except Exception:
                logo = self.driver.find_element(*LearnerDashboardLocators.LOGO)
                self.driver.execute_script("arguments[0].click();", logo)

            self.wait.until(EC.element_to_be_clickable(HomePageLocators.COURSES)).click()
            time.sleep(5)  

            course_cards = self.wait.until(EC.presence_of_all_elements_located((HomePageLocators.COURSE_CARDS)))
            
            visible_cards = []

            for card in course_cards:
                if card.is_displayed():
                    visible_cards.append(card) 
                    

            total_cards = len(visible_cards)
            print(f"Found {total_cards} visible course cards")

            if total_cards == 0:
                print("No visible course cards found.")
                return False

            selected_card = random.choice(visible_cards)

            self.driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", selected_card
            )
            time.sleep(1)
            self.driver.execute_script("arguments[0].click();", selected_card)
            print("Clicked on the random course card.")

            #open course detail page
            self.wait.until(EC.url_contains("/courses/details?id="))

            return True

        except Exception as e:
            print(f"Error selecting a course card: {e}")
            return False
        
    