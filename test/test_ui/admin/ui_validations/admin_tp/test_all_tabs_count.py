import logging

import pytest
from src.locators.admin_locators.admin_tp.admin_tp_locators import AdminTPLocators
from src.pages.admin_pages.dashboard.admin_dashboard import AdminDashboardPage
from src.pages.admin_pages.training_partners.admin_tp import AdminDashboardLocators, AdminTP


class TestAllTPs:
    
    @pytest.mark.smoke_checklist
    def test_all_tps_count(self, admin_logged_in):
        driver=admin_logged_in
        
         
        admin_dashboard=AdminDashboardPage(driver)
        admin_dashboard.click_menu_option("tp")
       
        admin_tp = AdminTP(driver) 
        for tab_name,option in AdminTP.TABS.items():     
            count = admin_tp.get_status_count(option["locator"])
            assert count > 0, "Error getting {} Count"
            logging.info(f"{tab_name} has {count} count")
            rows=admin_tp.get_no_of_rows_in_all_pages()
            assert rows==count, f"{tab_name}({count}) does not match with Number of rows present in {tab_name} : {rows}"
            logging.info(f"{tab_name}({count}) match with number of rows present in {tab_name} List: {rows}")



        # count = admin_tp.get_status_count(AdminTPLocators.AllTPSCount)
        # assert count > 0, "Error getting All TPs Count"
        # all_tps=admin_tp.get_no_of_rows_in_all_pages(count)
        # assert all_tps==count, f"All TPs({count}) does not match with Number of rows present in All TPs List "
        # print(f"All TPs({count}) match with number of rows present in All TPs List: {all_tps}")

        


