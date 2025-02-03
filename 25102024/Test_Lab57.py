#Drag and drop action

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def test07_mouse():
    # Set up the WebDriver (e.g., Chrome)
    driver = webdriver.Chrome()

    # Navigate to a webpage with drag-and-drop functionality
    driver.get("https://jqueryui.com/droppable/")
    driver.maximize_window()

    # Switch to the frame that contains the drag-and-drop elements (if needed)
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    # Locate the elements for drag and drop
    source_element = driver.find_element(By.ID, "draggable")  # Element to be dragged
    target_element = driver.find_element(By.ID, "droppable")  # Element to drop onto

    # Perform the drag-and-drop action
    actions = ActionChains(driver)
    actions.drag_and_drop(source_element, target_element).perform()
    time.sleep(5)

    # Verify the drop (e.g., by checking the target's text or class)
    result_text = target_element.text
    print("Result after dropping:", result_text)

    # Close the browser
    driver.quit()
