import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_01_radiobutton():
    driver = webdriver.Chrome()
    driver.get("http://qa-automation-practice.netlify.app/radiobuttons.html")
    driver.maximize_window()
    time.sleep(2)

    #Navigate to the webelement containing radio buttons
   # radio_element = driver.find_element(By.ID,"radio-button1").click()

    #Select multiple radio buttons at a time
    mulitple_element = driver.find_elements(By.XPATH,"//input[@type='radio']")
    print(mulitple_element)
    time.sleep(10)