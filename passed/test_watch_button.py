import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

def test_watch_button(driver):
    try:
        # Navigate to Pinterest website
        driver.get('https://www.pinterest.com/')
        print("Navigated to Pinterest website")

        # Wait until the Watch button is visible and interactable
        watch_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[1]/div[3]/a/div/div/span'))
        )                                          
        print("Located Watch button on Pinterest homepage")

        # Click on the Watch button
        watch_button.click()
        print("Clicked on Watch button")

        # Wait for the page to load (you can add more specific waits if necessary)
        time.sleep(5)

        # Example of further actions:
        # You can add assertions or further interactions with elements on the "Watch" page

        # Example assertion: Check if the page title contains 'Watch'
        assert "Watch" in driver.title
        print("Test Passed: Successfully navigated to Watch page.")

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

# Call the function to test the Watch button
test_watch_button(driver)
