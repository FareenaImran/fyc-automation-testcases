import random
import string
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from locators.learner_locators.home_page.course_detail_page.course_detail_page_locators import CourseDetailPageLocators
from locators.learner_locators.home_page.course_detail_page.enquiry_modal_locators import EnquiryModalLocators


class EnquiryModal(BasePage):   
    def send_enquiry(self):
      try:
        self.wait.until(EC.presence_of_element_located(CourseDetailPageLocators.LEARN_MORE))
        self.wait_and_click(CourseDetailPageLocators.LEARN_MORE)
        
        self.wait.until(EC.visibility_of_element_located(EnquiryModalLocators.ENQUIRY_LIGHTBOX))
        
        contact_method_dropdown = self.wait.until(EC.visibility_of_element_located(EnquiryModalLocators.CONTACT_METHOD))

        select=Select(contact_method_dropdown)
        options=select.options[1:]
        random_option=random.choice(options)
        select.select_by_visible_text(random_option.text)
        
        inquiry_type=self.driver.find_element(*EnquiryModalLocators.ENQUIRY_TYPE)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth',block:'center'});",inquiry_type)
     
        enquiry_type_dropdown=self.wait.until(EC.visibility_of_element_located(EnquiryModalLocators.ENQUIRY_TYPE))
        select=Select(enquiry_type_dropdown)
        options=select.options[1:]
        random_option=random.choice(options)
     
        select.select_by_visible_text(random_option.text)

        message_element=self.wait.until(EC.visibility_of_element_located(EnquiryModalLocators.ENQUIRY_MSG))
        prefix="Test Message - "
        remaining_length=256-len(prefix)
        random_message = prefix + ''.join(random.choices(string.ascii_letters + string.digits, k=remaining_length))
        message_element.send_keys(random_message)
        self.sent_msg=random_message
        print(f"\nMessage sent by Learner : {random_message}")

        send_inquiry=self.driver.find_element(*EnquiryModalLocators.SEND_ENQUIRY)
        self.driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth',block:'center'});",send_inquiry)
        self.wait_and_click(EnquiryModalLocators.SEND_ENQUIRY)
     
        time.sleep(5)
        return random_message
      
      except Exception as e:
          print ("Error sending an enquiry to TP")
          return None
    

    