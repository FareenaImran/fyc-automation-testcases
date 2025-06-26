from selenium.webdriver.common.by import By

class BaseLocators:
    
    #All Tables Rows
    ROWS=(By.XPATH,"//table[contains(@class,'w-full border-collapse')]/tbody/tr")

    #Pagination
    NEXT_BTN=(By.XPATH, "//button[contains(text(),'Next')]")
