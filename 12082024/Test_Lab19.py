import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@pytest.mark.positive
def test_vwo_login_invalid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com")

    driver.implicitly_wait(3)
    # e1, e2 , e3 ->
    # Tell Webdriver to wait for the 5 to Load
    # All the elements.
    # What if the e1,e2,e3 < 3, then 2 wasted

    username_element = driver.find_element(By.CSS_SELECTOR,"[name='username']")
    username_element.send_keys("admin@gmail.com")

    password_eement = driver.find_element(By.CSS_SELECTOR, "[name='password']")
    password_eement.send_keys("admin")

    button_submit_element = driver.find_element(By.ID, "js-login-btn")
    button_submit_element.click()

    time.sleep(5)  # This is Python Int who is waiting, Python Execution Halt.

    error_msg_element = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_msg_element.text)
    assert error_msg_element.text == "Your email, password, IP address or location did not match"
