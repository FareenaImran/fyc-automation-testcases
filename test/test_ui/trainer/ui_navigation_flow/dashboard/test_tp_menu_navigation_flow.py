import pytest
from src.utils.helpers.login_as_role import login_as_role
from src.utils.helpers.login_helper import login_with_credentials
from src.pages.tp_pages.dashboard.tp_dashboard_page import BasePage, TPDashboardPage



class TestTPDashboard():

    @pytest.mark.smoke_checklist
    def test_trainer_menu_options(self, trainer_logged_in):
        driver=trainer_logged_in
        
        basepage=BasePage(driver)
        basepage.is_model_present()

        tp_dashboard=TPDashboardPage(driver)
        for option in TPDashboardPage.MENU_OPTION:
            try:
                tp_dashboard.click_menu_option(option)
                assert tp_dashboard.is_menu_option_page_loaded(option),f"{option} page not loaded"
                print (f"{option.capitalize()} page loaded successfully")
            except Exception as e:
                print(f"Failed to load and verify {option} page:{e}")
                assert False
              

