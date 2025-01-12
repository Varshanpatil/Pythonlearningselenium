import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_sample():
    driver = webdriver.Chrome()
    driver.get("file:///D:/HTML%20project%20varsha/Login.html")

    #Find the element fot Firstname
    firstname_element = driver.find_element(By.ID,"user")

    # Find the element fot Last name
    lastname_element = driver.find_element(By.ID, "user")

    # Find the element fot password
    password_element = driver.find_element(By.ID, "user")


    #Find the element for emaild
    emailid_element = driver.find_element(By.CLASS_NAME,"mail")

    #Find the element for contact
    contact_element = driver.find_element(By.NAME,"contact")
    contact_element.click()
    time.sleep(5)

test_sample()