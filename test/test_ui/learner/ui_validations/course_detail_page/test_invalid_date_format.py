import re
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Pattern for invalid date format (e.g., May 15 2025)
def find_invalid_dates(text):
    pattern = r"\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|" \
              r"Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)\s+\d{1,2}\s+\d{4}\b"
    return re.findall(pattern, text)

def test_courses_with_invalid_date_format_and_matched_text(open_browser):
    driver = open_browser
    wait = WebDriverWait(driver, 20)
    invalid_entries = []

    driver.get("https://beta.findyourcourses.org/courses/all-courses")
    time.sleep(3)
    page_number = 1

    while True:
        print(f"\n--- Page {page_number} ---")

        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
        course_cards = driver.find_elements(By.CSS_SELECTOR, "div.group.cursor-pointer")

        for i in range(len(course_cards)):
            try:
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
                course_cards = driver.find_elements(By.CSS_SELECTOR, "div.group.cursor-pointer")
                card = course_cards[i]

                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", card)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", card)

                wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Enroll Now')]")))
                body_text = driver.find_element(By.TAG_NAME, "body").text

                invalid_dates = find_invalid_dates(body_text)
                if invalid_dates:
                    current_url = driver.current_url
                    print(f"Invalid date(s) found on: {current_url}")
                    for dt in invalid_dates:
                        print(f"   → Invalid Date: {dt}")
                        invalid_entries.append((current_url, dt))

            except Exception as e:
                print(f"Error on card #{i+1}: {e}")

            driver.back()
            try:
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
            except TimeoutException:
                time.sleep(2)
                wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.group.cursor-pointer")))
            time.sleep(2)

        # Pagination
        try:
            next_buttons = driver.find_elements(By.XPATH, "//button[contains(text(),'Next')]")
            if not next_buttons or next_buttons[0].get_attribute("disabled"):
                print("No more pages.")
                break

            print("Moving to next page...")
            driver.execute_script("arguments[0].click();", next_buttons[0])
            time.sleep(3)
            page_number += 1
        except Exception as e:
            print(f"Pagination error: {e}")
            break

    # Report
    if invalid_entries:
        print("\nCourses with invalid date format:")
        for url, dt in invalid_entries:
            print(f"{url}  —  Invalid Date: {dt}")

        with open("beta_invalid_date_details.log", "w") as f:
            for url, dt in invalid_entries:
                f.write(f"{url} — Invalid Date: {dt}\n")
    else:
        print("\nNo invalid date formats found in any course pages.")
