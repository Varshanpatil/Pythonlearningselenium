#wheel mouse action

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_02():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.apple.com/in")
    driver.maximize_window()
    time.sleep(3)

    #Locate  and airpod tareget element
    airpod_targetelement = driver.find_element(By.CSS_SELECTOR,"[data-analytics-title='learn more - apple watch ultra 2']")

    #Need to scroll down till airpod element
    action=ActionChains(driver)
    action.scroll_to_element(airpod_targetelement).perform()
    time.sleep(5)

    driver.quit()