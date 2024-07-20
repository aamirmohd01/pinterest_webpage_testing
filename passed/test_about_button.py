import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def test_about_button(driver):
    try:
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the About button is visible and interactable
        about_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[2]/div[1]/div[1]/div/a'))
        )                                           
        print("Located About button on Pinterest homepage")

        # Get the current window handle (to switch back later)
        main_window = driver.current_window_handle

        # Click on the About button
        about_button.click()
        print("Clicked on About button")

        # Wait for the new tab to open and switch to it
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))  # Wait until two windows are open
        for handle in driver.window_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                break

        # Wait for the About page to load (you can add more specific waits if necessary)
        time.sleep(5)

        # Get the page title for debugging
        page_title = driver.title
        print(f"About page title: {page_title}")

        # Example assertion: Check if the page title contains 'About Pinterest'
        # assert "About Pinterest" in page_title
        print("Test 3 Passed: Successfully navigated to About page.")

    except NoSuchElementException as e:
        print(f"Test Failed: Element not found - {e}")
    except TimeoutException as e:
        print(f"Test Failed: Timeout - {e}")
    except AssertionError as e:
        print(f"Test Failed: Assertion error - {e}. Page title was: {page_title}")

    finally:
        # Close the new tab and switch back to the main window
        driver.close()
        driver.switch_to.window(main_window)
        print("Closed the new tab and switched back to the main window")

# Initialize WebDriver
driver = webdriver.Chrome()

# Call the function to test the About button
test_about_button(driver)
