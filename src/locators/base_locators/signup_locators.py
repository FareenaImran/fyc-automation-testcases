from selenium.webdriver.common.by import By

class SignupLocators:
    FULL_NAME=(By.ID,"name")
    EMAIL=(By.ID,"email")
    C_NUMB=(By.ID,"contactNumber")
    PASSWORD=(By.ID,"password")
    C_PASSWORD=(By.ID,"confirmPassword")