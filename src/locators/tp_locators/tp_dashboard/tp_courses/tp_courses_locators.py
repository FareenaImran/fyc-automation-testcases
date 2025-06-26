from selenium.webdriver.common.by import By
class TPCoursesLocators:

    START_CREATING_COURSE=(By.XPATH,"//button[contains(text(),'Start Creating Course')]")

    #Tabs
    IN_PROGRESS=(By.XPATH,"//button[contains(text(),'In Progress')]")
    UNDER_REVIEW=(By.XPATH,"//button[contains(text(),'Under Review')]")