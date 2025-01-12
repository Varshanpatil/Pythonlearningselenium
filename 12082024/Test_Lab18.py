import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

def test_sample():
    driver = webdriver.Chrome()
    driver.get("file:///D:/HTML%20project%20varsha/login%20details.html")

    # Locate an element for Firstname
    Firstname_element = driver.find_element(By.XPATH,"/html/body/input[1]")
#   Firstname_element.click()
    time.sleep(2)

    #Locate an element for Lastname
    Lastname_element = driver.find_element(By.XPATH, "/html/body/input[2]")
#    Lastname_element.click()

    #locate an element for password
    password_element = driver.find_element(By.XPATH,"/html/body/input[3]")
#    password_element.click()

    # locate an element for Emailid
    email_element = driver.find_element(By.XPATH, "/html/body/input[4]")
#    email_element.click()

    # locate an element for country
    country_element = driver.find_element(By.XPATH, "/html/body/input[5]")
    country_element.click()






