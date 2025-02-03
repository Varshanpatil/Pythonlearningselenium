#right click action

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def test_03_mouse():
    # Step 1: Initialize the WebDriver
    driver = webdriver.Chrome()

    # Step 2: Navigate to the Google homepage
    driver.get("https://www.google.com")
    driver.maximize_window()

    # Step 3: Locate the search box and enter a query
    search_box = driver.find_element(By.NAME, "q")  # Locate the search box
    search_box.send_keys("Selenium WebDriver")  # Type a query

    # Step 4: Wait for the "Google Search" button to become interactable
    time.sleep(1)  # Allow the button to render (adjust timing if necessary)

    # Step 5: Locate the "Google Search" button
    search_button = driver.find_element(By.NAME, "btnK")

    # Step 6: Perform a right-click on the "Google Search" button
    action = ActionChains(driver)
    action.context_click(search_button).perform()

    # Step 7: Wait to observe the action
    time.sleep(3)

    # Step 8: Close the browser
    driver.quit()