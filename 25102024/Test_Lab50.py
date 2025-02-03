#WRT-Perform mouse vover action.1.Open website 2. Hover over developer then status.
#3.Status should be click and page will open
#Mouse hover action

import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

def test_02_mouse():
    driver = webdriver.Chrome()
    driver.get("https://www.browserstack.com/guide/mouse-hover-in-selenium")
    driver.maximize_window()
    time.sleep(5)

    #Navigate to the Developers webelement
    #developer = driver.find_element(By.ID,"developers-dd-toggle")
    developer = driver.find_element(By.XPATH,"//button[@id='developers-dd-toggle']")
    status = driver.find_element(By.LINK_TEXT,"Status")

    #Mouse hover action need to perform
    #Developer-->status
    action =ActionChains(driver)   #creating object for action
    action.move_to_element(developer).move_to_element(status).click().perform()
    time.sleep(5)
