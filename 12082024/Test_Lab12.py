import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def test_mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    assert driver.current_url == "https://app.vwo.com/#/login"

    email_web_element =driver.find_element(By.NAME,"username")
    email_web_element.click()
    email_web_element.send_keys("admin@admin.com")
    time.sleep(5)



test_mini_project_2()

