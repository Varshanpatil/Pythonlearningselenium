import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def move_slider_fixed_offset():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get("https://jqueryui.com/slider/")  # Example slider webpage
    driver.maximize_window()
    time.sleep(2)

    # Switch to the iframe containing the slider
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "demo-frame"))

    # Locate the slider handle
    slider = driver.find_element(By.CLASS_NAME, "ui-slider-handle")

    # Create an ActionChains object
    actions = ActionChains(driver)

    # Move the slider 100 pixels to the right
    actions.drag_and_drop_by_offset(slider, 100, 0).perform()
    time.sleep(5)

    time.sleep(2)
    driver.quit()

# Run the function
move_slider_fixed_offset()
