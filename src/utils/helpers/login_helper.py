from selenium.webdriver.support.ui import WebDriverWait

from src.base.login_page import LoginPage

def login_with_credentials(driver, role, email, password, url):
    driver.get(url)
    
    login_page = LoginPage(driver)
    login_page.login_credentials(email, password)

    if role in ["learner", "admin"]:
        login_page.login_button()
    else:
        login_page.tp_login_button()

    WebDriverWait(driver, 30).until(
        lambda d: "dashboard" in d.current_url.lower() or "profile" in d.page_source.lower()
    )

    assert "dashboard" in driver.current_url.lower() or "profile" in driver.page_source.lower()
    print(f"\nLogin successful for role: {role} - {email}\n")
