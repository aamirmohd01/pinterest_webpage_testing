import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# Initialize WebDriver (assuming Chrome here, adjust if using a different browser)
driver = webdriver.Chrome()

try:
    # Step 1: Open the Pinterest webpage
    driver.get('https://www.pinterest.com/')
    print("Navigated to Pinterest website")

    # Step 2: Test the "Explore" button
    try:
        explore_button_xpath = '//*[@id="__PWS_ROOT__"]/div/div[1]/div/div[1]/div/div[1]/div[4]/a/div/div/span'
        explore_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, explore_button_xpath))
        )
        print("Testing Explore button")
        explore_button.click()
        time.sleep(3)  # Wait for the page to load
        print("Successfully tested Explore button")

    except TimeoutException:
        print("Timeout while testing Explore button")
    except NoSuchElementException as e:
        print(f"Element not found while testing Explore button - {e}")

finally:
    # Close the browser session
    driver.quit()
    print("Closed the browser session")
