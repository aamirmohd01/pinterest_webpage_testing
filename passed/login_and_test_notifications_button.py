import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def login_and_test_notifications_icon(driver, email, password):
    try:
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the login button is visible and click it
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='simple-login-button']"))
        )
        login_button.click()
        print("Clicked login button")

        # Enter email and password
        email_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_field.send_keys(email)

        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        print("Entered email and password and logged in")

        # Wait for redirection after login
        WebDriverWait(driver, 10).until(
            EC.title_contains("Pinterest")
        )
        print("Logged in and home page loaded")

        # Locate the "Notifications" icon using aria-label attribute and class names
        notifications_icon = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Notifications' and contains(@class, 'S9z') and contains(@class, 'INd')]"))
        )
        notifications_icon.click()
        print("Clicked 'Notifications' icon")

        # Wait for the notifications dropdown or page to be displayed
        time.sleep(5)  # Adjust this delay if necessary

        # Validate that the notifications section or dropdown is displayed
        # Use appropriate selector here if available; for now, assuming some identification is needed
        notifications_dropdown = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'notifications-dropdown')]"))
        )
        if notifications_dropdown:
            print("Test Passed: Successfully navigated to notifications dropdown.")
        else:
            print("Test Failed: Notifications dropdown not displayed.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    finally:
        # End the session
        driver.quit()
        print("Closed the browser session")

# Initialize WebDriver
driver = webdriver.Chrome()

# Hardcoded credentials for login
username = '$$$$'
password = '$$$$'

# Call the function to login and test the "Notifications" icon
login_and_test_notifications_icon(driver, username, password)
