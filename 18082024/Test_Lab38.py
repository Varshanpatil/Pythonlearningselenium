import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_03_JS3():
    driver = webdriver.Chrome()
    driver.get("https://classic.crmpro.com/")
    driver.maximize_window()

    #scroll down till the forgot password element
    forgot_pwd = driver.find_element(By.LINK_TEXT, "Forgot Password?")
    driver.execute_script("arguments[0].scrollIntoView(true);", forgot_pwd)
    time.sleep(5)