from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)

driver.get("https://www.flipkart.com/")
# texti=driver.find_element(By.XPATH,"//td[contains(text(),'25')]//ancestor::table//td[starts-with(text(),'Selenium')]")
# print(f"{texti.text()}")

search_box=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,"//input[@type='text']")))
search_box.click()
search_box.send_keys("one plus")
options=driver.find_elements(By.XPATH,"//form[contains(@class,'header-form-search')]//a")
option_link=""
for index,option in enumerate(options):
    if "headphones" in option.text:
        print(f"index:{index}, option:{option.text}")
        option_link=option.get_attribute("href")
        option.click()
        break
else:
    print("headphones option not found")
assert option_link in driver.current_url, f"Navigated to the wrong page: {driver.current_url} != {option_link}"
