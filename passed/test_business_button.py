import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def test_businesses_button(driver):
    try:
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the Businesses button is visible and interactable
        businesses_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[2]/div/a'))
        )
        print("Located Businesses button on Pinterest homepage")

        # Get the current window handle (to switch back later)
        main_window = driver.current_window_handle

        # Click on the Businesses button
        businesses_button.click()
        print("Clicked on Businesses button")

        # Wait for the new tab to open and switch to it
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until two windows are open
        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # Example of further actions:
        # You can add assertions or further interactions with elements on the "Businesses" page

        # Example assertion: Check if the page title contains 'Business'
        assert "Business" in driver.title
        print("Test Passed: Successfully navigated to Businesses page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}")

    finally:
        # Close the new tab and switch back to the main window
        driver.close()
        driver.switch_to.window(main_window)
        print("Closed the new tab and switched back to the main window")

# Initialize WebDriver
driver = webdriver.Chrome()

# Call the function to test the Businesses button
test_businesses_button(driver)
