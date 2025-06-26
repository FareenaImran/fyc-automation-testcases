import shutil
import pytest
import sys
import os
from src.utils.helpers.login_as_role import login_as_role
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from src.utils.browser.browser_setup import get_chrome_driver


@pytest.fixture(scope="function")
def open_browser():
  driver = get_chrome_driver()
  yield driver
  driver.quit()

#Trainer
@pytest.fixture(scope="function")
def trainer_logged_in(open_browser):
    try:
        login_as_role(open_browser,"trainer")
    except Exception as e:
        print(f"Login failed for trainer . Error: {e}")
        assert False

    return open_browser

#Learner
@pytest.fixture(scope="function")
def learner_logged_in(open_browser):
    try:
        login_as_role(open_browser,"learner")
    except Exception as e:
        print(f"Login failed for trainer . Error: {e}")
        assert False

    return open_browser

#Admin
@pytest.fixture(scope="function")
def admin_logged_in(open_browser):
    try:
        login_as_role(open_browser,"admin")
    except Exception as e:
        print(f"Login failed for trainer . Error: {e}")
        assert False

    return open_browser

def pytest_sessionfinish(session, exitstatus):
    os.system("allure generate reports/allure-results -o reports/allure-report --clean")
    os.system("start reports/allure-report/index.html")
    