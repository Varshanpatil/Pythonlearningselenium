#How to handle slider movement

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test01_slider():
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/demoSite/practice/slider/range.html")
    driver.maximize_window()
    time.sleep(3)

    #Locate the minimum and maximum range webelement
    min_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
    max_slider  = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

    print(min_slider.location) #{'x': 227, 'y': 47}
    print(max_slider.location) #{'x': 910, 'y': 47}

    #Create object for actions
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(min_slider,400,0).perform()
    actions.drag_and_drop_by_offset(max_slider,-100,0).perform()

    print(min_slider.location) #{'x': 628, 'y': 47}
    print(max_slider.location) #{'x': 810, 'y': 47}
