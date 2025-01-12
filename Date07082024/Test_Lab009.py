#Write a program- 1. Open orangehrm website 2. find the element for "Book a free demo" button
# 3.click on "Booka free demo" button 4.Check the current url of th ewebsite 5. quit the browser
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_mini_project2():
    driver = webdriver.Chrome()
    driver.get("https://www.orangehrm.com/")
    # - Find the element the anchor tag
    # We need to find the unique attribute which can find the web element
    Booka_free_demo_element = driver.find_element(By.ID, "Form_submitForm_EmailHomePage")

    # - Click on it
    Booka_free_demo_element.click()
    driver.maximize_window()
    time.sleep(5)

test_mini_project2()
