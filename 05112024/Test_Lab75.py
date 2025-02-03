#Handl window example
#Open 2 website in same window


import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_05_windows():
    driver = webdriver.Chrome()
    driver.get("https://www.salesforce.com/au/")
    driver.maximize_window()
    time.sleep(3)
    driver.switch_to.new_window()   #It will open new tab with mentioned website below  on same window
    time.sleep(3)
    driver.get("https://www.orangehrm.com/en/orangehrm-starter-open-source-software")

    total_tab = len(driver.window_handles)
    print(total_tab)

    value = driver.window_handles
    print(value)

    #It will show which is current tab is on with their 16 digit code no
    current_tab = driver.current_window_handle
    print(current_tab)

    driver.quit()

