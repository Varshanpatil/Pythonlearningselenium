#Back click
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_08_mouse():
    # Set up the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    print("Current URL:", driver.current_url)
    time.sleep(5)

    # Navigate to another URL
    driver.get("https://youtube.com")
    print("Current URL after navigating:", driver.current_url)
    time.sleep(5)

    # Go back to the previous page
    driver.back()
    time.sleep(5)
    print("URL after back click:", driver.current_url)

    # Close the browser
    driver.quit()
