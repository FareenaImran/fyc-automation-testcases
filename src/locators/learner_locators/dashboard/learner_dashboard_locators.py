from selenium.webdriver.common.by import By

class LearnerDashboardLocators():

    #Logo
    LOGO=(By.CSS_SELECTOR,"div.flex.items-center.space-x-2 > a")
    #Side Menu Options
    DASHBOARD=(By.XPATH,"//li[.//span[text()='Dashboard']]")
    MYCOURSES=(By.XPATH,"//li[.//span[text()='My Courses']]")
    PROFILE=(By.XPATH,"//li[.//span[text()='Profile']]")
    ASSESSMENT=(By.XPATH,"//li[.//span[text()='Assessment']]")
    JOBS=(By.XPATH,"//li[.//span[text()='Jobs']]")
    SETTINGS=(By.XPATH,"//li[.//span[text()='Settings']]")



