#https://book.spicejet.com/Login.aspx

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


#Open chrome browser
def test_106():
    driver = webdriver.Chrome()
    driver.get("https://book.spicejet.com/Login.aspx")
    driver.maximize_window()
    #driver.implicitly_wait(2)
    time.sleep(10)

    #Locate the "round trip" webelement
    #round_trip = driver.find_element(By.CLASS_NAME,"selected-label")

    time.sleep(10)
    round_trip = driver.find_element(By.XPATH,"//label[@class='selected-label']")
    round_trip.click()

    #Locate the departure city webelement
    #departure = driver.find_element(By.LINK_TEXT,"Departure City")

