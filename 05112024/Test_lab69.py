#How to handle slider movement

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test02_slider():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(3)

    #search_element = driver.find_elements(By.XPATH, "//*[@id='placeholder']")
    search_element = driver.find_element(By.NAME, "q")
    search_element.click()
    search_element.send_keys("Sofa"+Keys.ENTER)

    time.sleep(5)

    #Locate the min and max element and print their x & y location
    min_element = driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[1]/div/div/div/section[2]/div[3]/div[1]/div[1]")
    max_element = driver.find_element(By.XPATH,"//*[@id='container']/div/div[3]/div/div[1]/div/div/div/section[2]/div[3]/div[1]/div[2]")
    time.sleep(5)

    print(min_element.location)  #{'x': 10, 'y': 476}
    print(max_element.location)  #{'x': 254, 'y': 476}

    # Create object for actions
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(min_element,50,0).perform()
    actions.click_and_hold(min_element).pause(1).release().perform()

    actions.drag_and_drop_by_offset(max_element,-100,0).perform()
    actions.click_and_hold(max_element).pause(1).release().perform()

    print(min_element.location)   #{'x': 50, 'y': 526}
    print(max_element.location)   #{'x': 175, 'y': 526}
    time.sleep(10)
    driver.quit()


