from selenium.webdriver.common.by import By
class EnquiryModalLocators:
    ENQUIRY_LIGHTBOX=(By.CSS_SELECTOR,"div.bg-white.rounded-xl")
    CONTACT_METHOD=(By.NAME,"contactMethod")
    ENQUIRY_TYPE=(By.NAME,"inquiryType")
    ENQUIRY_MSG=(By.NAME,"message")
    SEND_ENQUIRY=(By.XPATH,"//button[text()='Send Enquiry']")
