from selenium.webdriver.common.by import By

class TPDashboardLocators:
   
    #Lets Setup Your Profile
    MODAL=(By.XPATH,"//div[@role='dialog' and @id='radix-:r2:']")

    CLOSE_MODAL_BUTTON = (By.CSS_SELECTOR, 'button.absolute.right-4.top-4')


    #TP DATA
    TP_USERNAME=(By.XPATH,"//div[contains(@class,'user-name')]/p") 

    #Side menu options
    MENU_DASHBOARD=(By.XPATH,"//button[.//span[text()='Dashboard']]")
    MENU_PROFILE=(By.XPATH,"//button[.//span[text()='Profile']]")
    MENU_COURSE=(By.XPATH,"//button[.//span[text()='Courses']]")
    MENU_LEARNER=(By.XPATH,"//button[.//span[text()='Learners']]")
    MENU_SETTINGS=(By.XPATH,"//button[.//span[text()='Settings']]")


    #MENU_LOGOUT=(,"")