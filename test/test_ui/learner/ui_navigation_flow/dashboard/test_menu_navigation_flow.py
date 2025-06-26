import pytest
from src.pages.tp_pages.dashboard.tp_dashboard_page import BasePage
from src.utils.helpers.login_as_role import login_as_role

from src.pages.learner_pages.dashboard.learner_dashboard_page import LearnerDashboardPage

class TestLearnerDashboard():
 
 @pytest.mark.smoke_checklist
 def test_learner_dashboard_menu_options(self,learner_logged_in):
  driver=learner_logged_in

  basepage=BasePage(driver)
  basepage.is_model_present()

  l_dashboard=LearnerDashboardPage(driver)
  
  for option in LearnerDashboardPage.MENU_OPTION:
    try:
        l_dashboard.click_menu_option(option)
        assert l_dashboard.is_menu_option_page_loaded(option), f"{option} page not loaded"
        print(f"{option.capitalize()} page loaded successfully")
    except Exception as e:
        print(f"Failed to load and verify {option} page: {e}")
        assert False



