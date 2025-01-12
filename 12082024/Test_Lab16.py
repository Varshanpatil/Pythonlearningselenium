#Write a program to click on forgot account button link in facebook

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/login/")

    #find the element for "Forgpt account link button
    #anchor_element = driver.find_element(By.LINK_TEXT,"Forgotten account?")
    anchor_element = driver.find_element(By.PARTIAL_LINK_TEXT,"Forgotten")
    anchor_element.click()
    time.sleep(2)