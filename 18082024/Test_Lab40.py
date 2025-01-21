

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_02_alerts():
    driver = webdriver.Chrome()
    driver.get("https://mypage.rediff.com/login/dologin")
    driver.maximize_window()

    #Navigate to the Login button and click on it
    login_element = driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(5)

    # Now you can intereact with the alert using driver.switch_to_alert method
    alert = driver.switch_to.alert.accept()
    #alert.accept()
    driver.close()
