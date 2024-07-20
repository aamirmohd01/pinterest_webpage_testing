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

    # Step 3: Locate and click on a photo from the grid
    try:
        # Find a photo using the `data-test-id` attribute
        photo_xpath = '//div[@data-test-id="non-story-pin-image"]/div/img'
        photo = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, photo_xpath))
        )
        print("Testing photo click")
        photo.click()
        time.sleep(5)  # Wait for photo to open
        print("Successfully clicked on the photo")

    except TimeoutException:
        print("Timeout while clicking on photo")
    except NoSuchElementException as e:
        print(f"Element not found while clicking on photo - {e}")
    except Exception as e:
        print(f"An error occurred while clicking on photo - {e}")

    # Step 4: Save the post
    try:
        # Locate and click on the save button
        save_button_xpath = '//button[@aria-label="Save"]'
        save_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, save_button_xpath))
        )
        print("Testing Save button click")
        save_button.click()
        time.sleep(5)  # Adjust as needed
        print("Successfully saved the post")

    except TimeoutException:
        print("Timeout while clicking on Save button")
    except NoSuchElementException as e:
        print(f"Element not found while clicking on Save button - {e}")
    except Exception as e:
        print(f"An error occurred while clicking on Save button - {e}")

    # Step 5: Click on the Follow button
    try:
        # Locate and click on the follow button
        follow_button_xpath = '//button[@aria-label="Follow"]'
        follow_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, follow_button_xpath))
        )
        print("Testing Follow button click")
        follow_button.click()
        time.sleep(5)  # Adjust as needed
        print("Successfully followed")

    except TimeoutException:
        print("Timeout while clicking on Follow button")
    except NoSuchElementException as e:
        print(f"Element not found while clicking on Follow button - {e}")
    except Exception as e:
        print(f"An error occurred while clicking on Follow button - {e}")

finally:
    # Step 6: Close the browser session
    driver.quit()
    print("Closed the browser session")
