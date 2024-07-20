import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def login_and_test_settings_button(driver, email, password):
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

        # Locate the "Accounts and more options" button and click it
        accounts_options_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='header-accounts-options-button']"))
        )
        accounts_options_button.click()
        print("Clicked 'Accounts and more options' button")

        # Wait for options menu to be displayed
        time.sleep(5)  # Adjust this delay if necessary

        # Locate and click the "Settings" button
        settings_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@data-test-id='header-menu-options-settings']"))
        )
        settings_button.click()
        print("Clicked 'Settings' button")

        # Validate that the settings page is displayed
        WebDriverWait(driver, 10).until(
            EC.url_contains("settings")
        )
        print("Test Passed: Successfully navigated to the settings page.")
        
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

# Call the function to login and test the "Settings" button
login_and_test_settings_button(driver, username, password)
