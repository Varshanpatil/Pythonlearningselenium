#Handle Date picker

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_03_autosuggestion():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.globalsqa.com/demo-site/datepicker/")

    #Switching to the iframe
    

    #Locate Date webelement-webelement is in iframe so we need to switch to the iframe
    date = driver.find_element(By.XPATH,"//input[@id='datepicker']")


