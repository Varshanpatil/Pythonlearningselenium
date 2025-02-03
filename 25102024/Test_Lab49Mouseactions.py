#WRT -
#right click  mouse action

import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_02_mouse():
    # Step 1: Initialize the WebDriver
    driver = webdriver.Chrome()

    # Step 2: Navigate to the website
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    driver.maximize_window()
    time.sleep(5)

    # Step 3: Locate the element to right-click
    right_click_element = driver.find_element(By.XPATH, "//span[text()='right click me']")

    # Step 4: Perform the right-click (context click) action
    action = ActionChains(driver)
    action.context_click(right_click_element).perform()

    # Step 5: Wait and observe the result
    time.sleep(3)

    # Step 6: Close the browser
    driver.quit()




