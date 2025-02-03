#Handle window-
# 1.New Tab:Opens a new tab and switches to a new tab
# 2. New Window-Opens a new browser window and switches to a new window

import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_02_windows():
    driver = webdriver.Chrome()

    #New Tab-selenium 4:Opens a new tab and switches to a new tab
    #driver.get("https://www.opencart.com/")
    #driver.switch_to.new_window('tab')
    #driver.get("https://www.orangehrm.com/")

    #New Window-selenium 4-Opens a new browser window and switches to a new browser window
    driver.get("https://www.opencart.com/")
    driver.switch_to.new_window('window')
    driver.get("https://www.orangehrm.com/")

    driver.quit()


