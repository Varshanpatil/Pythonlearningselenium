#WRT- using javascript executor create a alert and prompt on mentioned webpage

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_02_JS2():
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()

    #Javascript executor-Alert
    driver.execute_script("alert('Varsha patil/Chaudhari')")
    time.sleep(10)
    
    #Javascript executor-Prompt
   # driver.execute_script("prompt('Enter your name?')")
    time.sleep(10)

test_02_JS2()