#Handle Autosuggestion in selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_03_autosuggestion():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
    driver.implicitly_wait(10)

    # Locate the input field and type a character
    tags = driver.find_element(By.ID,"tags")
    tags.click()
    tags.send_keys("S")

    # Locate and print suggestion list elements
    list_elements = driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']//div")
    #print("Total suggestions are" , len(list_elements))

    print(f"Number of suggestions: {len(list_elements)}")
    for ele in list_elements:
        if ele.text =='Selenium':
            print("Record found")
            ele.click()
            break




