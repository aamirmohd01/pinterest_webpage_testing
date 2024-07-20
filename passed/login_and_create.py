import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Hardcoded test data
    website = 'https://www.pinterest.com/login/'
    username = '$$$$'
    password = '$$$$'

    # Step 1: Navigate to the website
    driver.get(website)
    print("Navigated to website")

    # Check if we are on the Pinterest login page
    assert "Pinterest" in driver.title
    print("Title check passed")

    # Step 2: Locate and interact with web elements to log in
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

        # Wait for login to complete
        time.sleep(5)
        print("Login process initiated")

        # Assert login was successful by checking the presence of a known post-login element
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="HeaderContent"]/div/div/div[2]/div/div/div/div[1]'))
        )
        print("Test Passed: Login successful.")
    
    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    # Step 3: Find and test the "Create" button using full XPath
    try:
        create_button_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[4]/div/a/div/div/span'
        create_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, create_button_xpath))
        )
        print("Testing Create button")
        create_button.click()
        time.sleep(3)  # Adjust as needed
        print("Successfully tested Create button")

    except TimeoutException:
        print("Timeout while testing Create button")
    except NoSuchElementException as e:
        print(f"Element not found while testing Create button - {e}")
    except Exception as e:
        print(f"An error occurred while testing Create button - {e}")

finally:
    # Step 4: Close the browser session
    driver.quit()
    print("Closed the browser session")
