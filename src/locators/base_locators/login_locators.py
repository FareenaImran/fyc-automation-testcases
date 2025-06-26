from selenium.webdriver.common.by import By

class BaseLoginLocators:
    
    EMAIL=(By.ID,"email")
    PASSWORD=(By.ID,"password")
    CONTINUE=(By.XPATH, "//button[@type='submit']")

class TPLoginLocators(BaseLoginLocators):
    LOGIN=(By.XPATH,"//button[@type='submit' and text()='Continue']")