#Write a program
# 1.Open a chrome browser
# 2. Open facebook
# 3.Remove EMAIL ID
# 4.Enter the mobile no
# 5.Enter Password

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def sample_practice_01():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login/")
    assert driver.current_url == "https://www.facebook.com/login/"

    #Find the element for emai ld adress
    emailid_webelement = driver.find_element(By.ID,"email")
    emailid_webelement.click()
    emailid_webelement.send_keys("admin@123.com")
    time.sleep(5)

    #Remove the wrong email from emai id field
    emailid_webelement.clear()
    time.sleep(2)

    #Enter the mobile no in email id field
    emailid_webelement.send_keys("9867678980")
    time.sleep(2)

    #find the element for password fileds
    emailid_webelement = driver.find_element(By.ID,"pass")


sample_practice_01()
