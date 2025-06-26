from selenium.webdriver.common.by import By
class CourseDetailPageLocators:   
    LEARN_MORE=(By.XPATH,"//button[text()='Learn More']")
    TP_COURSES=(By.CSS_SELECTOR,"div.group.relative.h-auto.bg-white.rounded-lg.cursor-pointer")
    COURSES_TAB=(By.XPATH,"//button[@role='tab' and contains(text(),'Courses')]")