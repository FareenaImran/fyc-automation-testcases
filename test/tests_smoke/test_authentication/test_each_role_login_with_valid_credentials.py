import pytest
from selenium.webdriver.common.by import By

from utils.helpers.login_as_role import login_as_role


class TestAuthentication:

    @pytest.mark.smoke_checklist
    @pytest.mark.parametrize("role", ["learner", "trainer", "admin"])
    def test_verify_login_with_valid_credentials(self, open_browser, role):
        driver = open_browser
        try:
            user_data = login_as_role(driver, role)
        except Exception as e:
            print(f"\nLogin failed for role: {role}. Error: {e}")
            assert False
