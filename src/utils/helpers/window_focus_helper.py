import time
from selenium.webdriver.support.ui import WebDriverWait

def wait_until_window_focused(driver, timeout=10):
    """Wait until the current browser window has JS-level focus (document.hasFocus())."""
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script("return document.hasFocus();")
    )