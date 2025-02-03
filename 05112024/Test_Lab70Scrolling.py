#How to handle Scrolling webpage vertically with using javascript executor


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def test01_scroll():

    driver = webdriver.Chrome()
    driver.implicitly_wait(15)

    driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
    driver.maximize_window()
    time.sleep(10)

    #1.scroll down page by pixel
    #driver.execute_script("window.scrollBy(0,3000)")
    #value = driver.execute_script("return window.pageYOffset;")
    #print("Number of pixels moved;",value)  #3000
    #time.sleep(10)

    #2.scroll downpage till the element is visible
    #flag = driver.find_element(By.XPATH,"//img[@alt='Flag of Afghanistan']")
    #driver.execute_script("arguments[0].scrollIntoView();", flag)
    #value1 = driver.execute_script("return window.pageYOffset;")
    #print("Number of pixels moved;", value1)

    #3 scroll down page till the end
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
    value2 = driver.execute_script("return window.pageYOffset;")
    print("Number of pixels moved;", value2)
    time.sleep(10)

    #4 scoll up to position
    driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
    value3 = driver.execute_script("return window.pageYOffset;")
    print("Number of pixels moved;", value3)
    time.sleep(10)
    driver.quit()

