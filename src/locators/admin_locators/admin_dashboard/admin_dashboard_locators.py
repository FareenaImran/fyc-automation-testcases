from selenium.webdriver.common.by import By
class AdminDashboardLocators:
    DASHBOARD = (By.XPATH, "//li[.//span[contains(text(),'Dashboard')]]")
    TP= (By.XPATH, "//li[.//span[contains(text(),'Training Partners')]]")
    COURSES = (By.XPATH, "//li[.//span[contains(text(),'Courses')]]")
    OFFERINGS = (By.XPATH, "//li[.//span[contains(text(),'Offerings')]]")
    LEARNERS = (By.XPATH, "//li[.//span[contains(text(),'Learners')]]")
    USER_MANAGEMENT = (By.XPATH, "//li[.//span[contains(text(),'User Management')]]")
    SETTINGS= (By.XPATH, "//li[.//span[contains(text(),'Settings')]]")

    