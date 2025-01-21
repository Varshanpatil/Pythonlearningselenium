#Authentication popup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test_03_authpopup():
    driver = webdriver.Chrome()
    #driver.get("https://the-internet.herokuapp.com/basic_auth")

    #Using syntax we can handle this authentication popup
    driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    driver.maximize_window()
    time.sleep(5)