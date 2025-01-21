

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_01_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://artoftesting.com/samplesiteforselenium")
    driver.maximize_window()

    #Select specific single checkbox and click it
    single_element = driver.find_element(By.XPATH , "//input[@class='Automation']")
    single_element.click()
    time.sleep(5)

    #Select multiple checkbox at a time
    multiple_element = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    print(len(multiple_element))

    for i in range (len(multiple_element)):
        multiple_element[i].click()
        time.sleep(5)

    driver.close()


