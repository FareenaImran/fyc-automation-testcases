from src.base.base_page import BasePage
from src.pages.admin_pages.training_partners.admin_tp import AdminDashboardLocators


class AdminDashboardPage(BasePage):

    MENU_OPTION={
       "dashboard":{"locator":AdminDashboardLocators.DASHBOARD},
       "tp":{"locator":AdminDashboardLocators.TP},
       "courese":{"locator":AdminDashboardLocators.COURSES},
       "learners":{"locator":AdminDashboardLocators.LEARNERS},
       "offerings":{"locator":AdminDashboardLocators.OFFERINGS},
       "user_management":{"locator":AdminDashboardLocators.USER_MANAGEMENT}
    }

    def click_menu_option(self,option_name):
        self.wait_and_click(self.MENU_OPTION[option_name]["locator"])