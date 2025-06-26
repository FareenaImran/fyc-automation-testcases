from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.tp_pages.dashboard.tp_learners.tp_enquiries.tp_enquiries_page import TPDashboardLocators
from src.utils.helpers.login_helper import login_with_credentials
from src.utils.test_data.csv_reader import get_random_credentials_from_google_sheet


def login_as_role(driver, role):
     user_data = get_random_credentials_from_google_sheet(role)
     login_with_credentials(driver, role, email=user_data["email"], password=user_data["password"], url=user_data["url"])
            
     return user_data