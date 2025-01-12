import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException,
                                        ElementNotSelectableException)
from selenium.webdriver.support.ui import Select

def test_vwo_login_select():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")
    driver.maximize_window()
    element_select = driver.find_element(By.ID,"dropdown")
    #create class object for select
    select = Select(element_select)
    #select.select_by_index(2)
    #select.select_by_visible_text("Option 2")
    #select.select_by_visible_text("Option 1")
    time.sleep(5)
