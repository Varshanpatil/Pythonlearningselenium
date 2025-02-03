#Handle windows (Parent window and child window)

import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_01_windows():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()

    #We will get parent window URL using this
    parent_window = driver.current_window_handle  # 1
    print(parent_window)

    #Locate the element to click on link
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()

    #It will share present all present tab in that window
    window_handles = driver.window_handles  # 2-currently 2 window is open
    print(window_handles)
    time.sleep(5)

    for handle in window_handles:
        driver.switch_to.window(handle)  # child
        if "New Window" in driver.page_source:
            print("Testcase Passed!!")
            break

     #way 2-Without using for loop, we can directly call any window using this below command
    #driver.switch_to.window(window_handles[1])
    #driver.switch_to.window(window_handles[3])  #If 3 website is there,you can put directly no here
    time.sleep(5)

    driver.quit()


