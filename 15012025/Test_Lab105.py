
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_105():
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
    driver.maximize_window()
    time.sleep(2)

    #Locate dropdown element
    dropdown_element = driver.find_element(By.LINK_TEXT,"Afghanistan")
