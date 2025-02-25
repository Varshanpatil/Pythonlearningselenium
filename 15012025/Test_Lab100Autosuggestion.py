#Handle Autosuggestion in selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_01_autosuggestion():
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")
    driver.maximize_window()
    time.sleep(2)

    #Locate the search bar webelement
    search_bar = driver.find_element(By.XPATH,"//input[@placeholder='Search for Products, Brands and More']").send_keys("Mac")

    #Locate one of the item from autosuggestion
    mac_mini4 = driver.find_elements(By.CLASS_NAME,"YGcVZO _2VHNef")


    #Need to print all the autosuggestion details present in the dropdown
    for search_bar in mac_mini4:
        print(search_bar.text)


