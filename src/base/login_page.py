from src.base.base_page import BasePage
from src.locators.base_locators.login_locators import BaseLoginLocators, TPLoginLocators

class LoginPage(BasePage):
    def login_credentials(self, email, password):

        try:
            self.wait_and_type(BaseLoginLocators.EMAIL, email)
            self.wait_and_type(BaseLoginLocators.PASSWORD, password)
            self.logger.info(f"Entered credentials for email: {email}")
        except Exception as e:
            self.logger.error(f"Failed to enter credentials: {str(e)}")
            raise

    def login_button(self):
        """Click login button for learner and admin"""
        try:
            self.wait_and_click(BaseLoginLocators.CONTINUE)
            self.logger.info("Clicked on continue button")
        except Exception as e:
            self.logger.error(f"Failed to click login button: {str(e)}")
            raise

    def tp_login_button(self):
        """Click login button for Training Provider"""
        try:
            self.wait_and_click(TPLoginLocators.LOGIN)
            self.logger.info("Clicked on TP login button")
        except Exception as e:
            self.logger.error(f"Failed to click TP login button: {str(e)}")
            raise



     
