import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Hardcoded test data
    website = 'https://www.pinterest.com/login/'
    username = '$$$$'
    password = '$$$$'

    # Step 3: Navigate to the website
    driver.get(website)
    print("Navigated to website")

    # Check if we are on the Pinterest login page
    assert "Pinterest" in driver.title
    print("Title check passed")

    # Step 4: Locate and interact with web elements
    try:
        # Find the username and password fields
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        print("Located username and password fields")
        
        # Enter the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        print("Entered username and password")

        # Assert login was successful
        time.sleep(5)  # Wait for the page to load
        if "Pinterest" in driver.title:
            print("Test Passed: Login successful.")
        else:
            print("Test Failed: Login unsuccessful.")
    
    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

finally:
    # Step 6: End the session
    driver.close()
    print("Closed the browser session")
