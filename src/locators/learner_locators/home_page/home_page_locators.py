from selenium.webdriver.common.by import By
class HomePageLocators:
    
    #Courses
    COURSES=(By.XPATH,"//a[@href='/courses/all-courses' and text()='Courses']")
    COURSE_CARDS=(By.CSS_SELECTOR,"div.group.cursor-pointer")

    #Training Partner
    TRAINING_PARTNERS=(By.XPATH,"//a[@href='/training-partner']")
    TP_CARDS=(By.CSS_SELECTOR,"div.group.cursor-pointer")
    TP_TITLE=(By.XPATH,"//div[contains(@class,'p-4') and contains(@class,'pt-14')]/h3")

    