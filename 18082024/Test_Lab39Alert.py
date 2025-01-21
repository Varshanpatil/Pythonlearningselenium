#WRT-Need to hanled prompt alert and type Pramod and accept the alert or dismiss the alert

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_01_alerts():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()

    #Navigate to the JS PROMPT element
    button = driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']")
    button.click()

    #wait for the alert to appear
    wait = WebDriverWait(driver, 10)
    wait.until(EC.alert_is_present())

    #Now you can intereact with the alert using driver.switch_to_alert method
    alert = driver.switch_to.alert
    alert.send_keys("Pramod")
    alert.accept()
    # alert.dismiss()

    # popups -> model or html popup, alert - this how handle
    # wait for the model to come and click on the escape button, or close button
    result = driver.find_element(By.ID, "result")
    print(result.text)
    assert "Pramod" in result.text
    time.sleep(10)
    driver.quit()

test_01_alerts()