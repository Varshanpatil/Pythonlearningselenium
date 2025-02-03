##Double click action
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def test_05_mouse():
    # Step 1: Initialize the WebDriver
    driver = webdriver.Chrome()

    # Step 2: Navigate to the demo website
    driver.get("https://api.jquery.com/dblclick/")
    driver.maximize_window()

    # Step 3: Switch to the iframe containing the demo
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    # Step 4: Locate the box to double-click
    box = driver.find_element(By.CSS_SELECTOR, "div")

    # Step 5: Perform the double-click action
    action = ActionChains(driver)
    action.double_click(box).perform()

    # Step 6: Wait to observe the result
    time.sleep(3)

    # Step 7: Close the browser
    driver.quit()
