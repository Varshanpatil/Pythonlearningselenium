#Write a program-Select dropdwon in jobtitle and select "It manager"
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

def saleforece_login():
    driver = webdriver.Chrome()
    driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")

    #Need to find element for Job title
    #driver = driver.find_element(By.ID,"UserTitle-GFlH")

    #select = Select()
