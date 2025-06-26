import time
import pytest
from src.pages.learner_pages.dashboard.learner_dashboard_page import LearnerDashboardPage
from src.pages.learner_pages.home.courses_tab.course_detail_page.enquiry_modal import EnquiryModal
from src.pages.learner_pages.home.training_partners_tab.tp_listing_page import TPListingPage
from src.pages.tp_pages.dashboard.tp_dashboard_page import TPDashboardPage
from src.pages.tp_pages.dashboard.tp_dashboard_page import TPDashboardPage
from src.pages.tp_pages.dashboard.tp_learners.tp_enquiries.tp_enquiries_page import TPEnquiriesPage
from src.utils.browser.browser_setup import get_chrome_driver
from src.utils.helpers.login_as_role import login_as_role
from src.utils.helpers.login_helper import login_with_credentials
from src.utils.test_data.csv_reader import get_untried_trainer
from src.utils.helpers.window_focus_helper import  wait_until_window_focused


class TestEnquiryFlows:
     
   @pytest.mark.smoke_checklist
   def test_flow(self, open_browser):
    max_attempts = 10
    attempt = 0
    tried_emails = set()
    
    tp_driver = open_browser
    trainer_window=tp_driver.current_window_handle
    tp_driver.switch_to.window(trainer_window)
    tp_driver.execute_script("window.focus();")  # JS focus

    while attempt < max_attempts:
        try:
            trainer = get_untried_trainer(tried_emails)
            tp_email = trainer["email"]
            print(f"\nAttempt {attempt + 1}: Trying login with email: {tp_email}")

            login_with_credentials(tp_driver, "trainer", trainer["email"], trainer["password"], trainer["url"])
            tpdashboardpage = TPDashboardPage(tp_driver)
            tp_name = tpdashboardpage.get_tp_name()
            print(f"Logged in as {tp_name} - Email: {tp_email}")

            is_start_button_visible = tpdashboardpage.is_start_creating_course_button_present()
            in_progress_count, under_review_count = tpdashboardpage.get_course_count()

            print(f"(In Progress: {in_progress_count}) (Under Review: {under_review_count})")
            print(f"Start Creating Course button present? {is_start_button_visible}")

            if in_progress_count > 0 or under_review_count > 0:
                course_msg = []
                if in_progress_count > 0:
                    course_msg.append(f"{in_progress_count} In Progress")
                if under_review_count > 0:
                    course_msg.append(f"{under_review_count} Under Review")

                print(f"Valid TP found with {' and '.join(course_msg)} course(s). Proceeding...")
                break  # Exit the loop successfully
            else:
                print(f"TP has no courses. Blacklisting {tp_email} and retrying...")
                tried_emails.add(tp_email)
                tp_driver.quit()
                tp_driver = get_chrome_driver()
                trainer_window = tp_driver.current_window_handle  
                attempt += 1

        except Exception as e:
            print(f"Trainer login attempt {attempt + 1} failed: {e}")
            try:
                tried_emails.add(tp_email)
            except:
                pass

            # Add safety check here too
            try:
                tp_driver.quit()
            except:
                pass

            tp_driver = get_chrome_driver()
            attempt += 1

    if attempt >= max_attempts:
        pytest.fail(f"Could not find a TP with at least one course after {max_attempts} attempts.")
          
   #Open browser for learner

    l_driver=get_chrome_driver()
    try:
      user_data=login_as_role(l_driver,"learner")

      tpflow=TPListingPage(l_driver)
      navigatetohomepage=LearnerDashboardPage(l_driver)
      navigatetohomepage.navigate_to_home()
      open_tp=tpflow.select_and_open_specific_tp(tp_name)
      assert open_tp, f"TP '{tp_name}',has no course ."
      
   #Send Enquiry
      sendenquiry=EnquiryModal(l_driver)
      latest_enquiry=sendenquiry.send_enquiry()
      assert latest_enquiry ,f"Could not get input from send_enquiry()"
      
      time.sleep(3)  
      tp_driver.switch_to.window(trainer_window)
      tp_driver.execute_script("window.focus();")  # JS focus
      wait_until_window_focused(tp_driver)

      verifylatestenquiry=TPEnquiriesPage(tp_driver)
      
      tp_driver.refresh()
      current_url = tp_driver.current_url
      assert "login" not in current_url.lower(), "Trainer session expired, redirected to login"
      
      top_enquiry=verifylatestenquiry.get_latest_enquiry_msg_from_enquiries_table()
      assert top_enquiry,f"\nCould not get input from get_latest_enquiry_msg_from_enquiries_table()"
         
      assert latest_enquiry==top_enquiry,f"\nExpected '{latest_enquiry}' but got \n '{top_enquiry}'"
      print(f"\nEnquiry match confirmed!")
    except Exception as e:
         print(f"\nFailed to Verify Latest Enquiry {e}")
         assert False
      
    finally:
      l_driver.quit()
      tp_driver.quit()