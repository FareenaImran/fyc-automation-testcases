from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException
import time


def test_open_all_courses_and_check_nan_value(open_browser):
    driver = open_browser
    wait = WebDriverWait(driver, 20)
    nan_urls = []

    driver.get("https://staging.findyourcourses.org/courses/all-courses")
    time.sleep(3)
    
    page_number = 1
    while True:
        print(f"\nPage : {page_number}")

        try:
            wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
            course_cards = driver.find_elements(By.CSS_SELECTOR, "div.group.cursor-pointer")
            total_cards = len(course_cards)
            print(f"Found {total_cards} course cards")

            for i in range(total_cards):
                try:
                    # Re-fetch cards fresh before every click to avoid stale reference
                    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
                    course_cards = driver.find_elements(By.CSS_SELECTOR, "div.group.cursor-pointer")
                    card = course_cards[i]

                    print(f"Opened Course Card :{i+1}")

                    # Scroll and click
                    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                    time.sleep(1)

                    try:
                        driver.execute_script("arguments[0].click();", card)
                    except (StaleElementReferenceException, TimeoutException):
                        print(f"Retry clicking card #{i+1}")
                        time.sleep(2)
                        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
                        course_cards = driver.find_elements(By.CSS_SELECTOR, "div.group.cursor-pointer")
                        card = course_cards[i]
                        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                        time.sleep(1)
                        driver.execute_script("arguments[0].click();", card)

                    # Wait for detail page to load (enroll button)
                    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Enroll Now')]")))

                    # Extract Registration Fee text
                    try:
                        amount_element = driver.find_element(By.XPATH, "//p[@class='font-light']")
                        amount_text = amount_element.text.strip()
                    except NoSuchElementException:
                        amount_text = "N/A"
                    print(f"Registration Fee: {amount_text}")

                    if "NaN" in amount_text:
                        print(f"Found NaN on Course# {i+1} of Page# {page_number},\nHere is the course url:\n {driver.current_url}")
                        nan_urls.append(driver.current_url)

                except Exception as detail_err:
                    print(f"Error opening or checking course card: {i+1}: {detail_err}")

                driver.back()

                # Wait for the course cards container to reload
                try:
                    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
                except TimeoutException:
                    print("Timeout waiting for course cards after going back, retrying once...")
                    time.sleep(2)
                    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))

                time.sleep(2)  

            # Pagination: click Next if enabled
            try:
                next_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Next')]")
                if not next_buttons:
                    print("\n\nNo 'Next' button found. Assuming last page.")
                    break

                next_btn = next_buttons[0]
                disabled = next_btn.get_attribute("disabled")

                if disabled:
                    print("Last page reached.")
                    break
                else:
                    print("Clicking Next page ...")
                    driver.execute_script("arguments[0].click();", next_btn)
                    time.sleep(3)
                    page_number += 1

            except Exception as e:
                print(f"Unexpected error checking or clicking 'Next': {e}")
                break


        except Exception as outer_err:
            print(f"Error on page {page_number}: {outer_err}")
            break

    if nan_urls:
        print("\nNaN Value found on these course detail pages:")
        for url in nan_urls:
            print(url)
        with open("nan_urls.log", "w") as f:
            f.writelines(url + "\n" for url in nan_urls)
    else:
        print("\nNo NaN values found on any course pages.")
