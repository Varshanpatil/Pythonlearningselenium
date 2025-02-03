#right click action with handling alert

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

# Step 1: Initialize the WebDriver
driver = webdriver.Chrome()

# Step 2: Navigate to the website
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

# Step 3: Locate the element to right-click
right_click_element = driver.find_element(By.XPATH, "//span[text()='right click me']")

# Step 4: Perform the right-click (context click) action
action = ActionChains(driver)
action.context_click(right_click_element).perform()

# Step 5: Select an option from the context menu
# Wait for a short time to ensure the menu is visible
time.sleep(1)  # Optional, depending on page loading speed

# Locate the menu option to select (e.g., "Edit")
menu_option = driver.find_element(By.XPATH, "//li[contains(@class, 'context-menu-item') and .//span[text()='Edit']]")
menu_option.click()

# Step 6: Wait and observe the result (an alert appears)
time.sleep(3)

# Step 7: Handle the alert (if any)
alert = driver.switch_to.alert
print(f"Alert text: {alert.text}")
alert.accept()  # Click "OK" on the alert

# Step 8: Close the browser
driver.quit()
