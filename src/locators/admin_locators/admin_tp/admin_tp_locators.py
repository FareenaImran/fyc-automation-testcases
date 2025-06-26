from selenium.webdriver.common.by import By

class AdminTPLocators:
    AllTPSCount = (By.XPATH, "//button[contains(@class, 'px-3 py-1 text-sm') and contains(text(), 'All TPs')]")
    APPROVED=(By.XPATH,"//button[contains(@class,'px-3 py-1 text-sm') and contains(text(),'Approved')]")
    INPROGRESS=(By.XPATH,"//button[contains(@class,'px-3 py-1 text-sm') and contains(text(),'In Progress')]")
    UP_FOR_REVIEW=(By.XPATH,"//button[contains(@class,'px-3 py-1 text-sm') and contains(text(),'Up for review')]")
    NEEDS_ATTENTION=(By.XPATH,"//button[contains(@class,'px-3 py-1 text-sm') and contains(text(),'Needs Attention')]")
    UNPUBLISHED=(By.XPATH,"//button[contains(@class,'px-3 py-1 text-sm') and contains(text(),'Unpublished')]")
