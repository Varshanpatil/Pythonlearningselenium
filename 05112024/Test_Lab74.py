

import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_04_windows():
    driver = webdriver.Chrome()
    driver.get("https://www.salesforce.com/au/")
    driver.maximize_window()

    #Locate "Try for free" webelement on the webpage and click on it
    try_free = driver.find_element(By.CSS_SELECTOR,"[data-link-text='Try for free']")
    parent_win = driver.current_window_handle
    try_free.click()
    time.sleep(5)

    all_win_handle = driver.window_handles
    for i in all_win_handle:
        if parent_win != i:
            driver.switch_to.window(i)
            header = driver.find_element(By.XPATH,"//h1//span" )  #After clicking on try free new website will open in new tab->in which need to find webelement for "Start your free day trial"
            print(header.text)

    #Again switch to parent wondow
    driver.switch_to.window(parent_win)
    time.sleep(3)
    driver.quit()
