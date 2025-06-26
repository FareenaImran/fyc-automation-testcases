import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_chrome_driver():
    options = Options()  #Object to hold Chrome browser configuration options
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  #Hides the “Chrome is being controlled by automated software” infobar.
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--start-maximized")  # Maximize to make modal fully visible
    options.add_argument("--log-level=3")  #To reduce noise in the terminal
    driver = webdriver.Chrome(options=options)
    return driver