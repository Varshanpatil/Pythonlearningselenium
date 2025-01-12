#Write a program- 1. Open cura website 2. find the element for make button 3.click on make button 4.quit the browser
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure


def test_mini_project_1():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # - Find the element the anchor tag
    # We need to find the unique attribute which can find the web element
    make_appointment_element = driver.find_element(By.ID,"btn-make-appointment")

    # - Click on it
    make_appointment_element.click()
    time.sleep(5)

    # Verify that URL changes
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    driver.quit()

test_mini_project_1()