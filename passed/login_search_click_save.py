import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

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

    # Step 3: Find the search box using full XPath, enter "laptop", and test it
    try:
        search_box_xpath = '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div/div[5]/div/div/div[1]/input'
        search_box = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, search_box_xpath))
        )
        print("Testing Search box")
        search_box.click()
        search_box.send_keys("laptop")
        search_box.send_keys(Keys.RETURN)
        print("Successfully tested Search box with keyword 'laptop'")

        # Wait for search results to load
        time.sleep(5)  # Adjust as needed

    except TimeoutException:
        print("Timeout while testing Search box")
    except NoSuchElementException as e:
        print(f"Element not found while testing Search box - {e}")
    except Exception as e:
        print(f"An error occurred while testing Search box - {e}")

    # Step 4: Click on the search result
    try:
        result_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[4]/div/div[1]/div/div/div/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/a/div/div[1]/div/div/div/div/div/img'
        search_result = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, result_xpath))
        )
        print("Testing Search result click")
        search_result.click()
        time.sleep(5)  # Adjust as needed
        print("Successfully clicked on the search result")

    except TimeoutException:
        print("Timeout while clicking on search result")
    except NoSuchElementException as e:
        print(f"Element not found while clicking on search result - {e}")
    except Exception as e:
        print(f"An error occurred while clicking on search result - {e}")

    # Step 5: Find and click on the Save button
    try:
        save_button_xpath = '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div/div/div[2]/div/button/div/div'
        save_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, save_button_xpath))
        )
        print("Testing Save button click")
        save_button.click()
        time.sleep(5)  # Adjust as needed
        print("Successfully clicked on the Save button")

    except TimeoutException:
        print("Timeout while clicking on Save button")
    except NoSuchElementException as e:
        print(f"Element not found while clicking on Save button - {e}")
    except Exception as e:
        print(f"An error occurred while clicking on Save button - {e}")

finally:
    # Step 6: Close the browser session
    driver.quit()
    print("Closed the browser session")
