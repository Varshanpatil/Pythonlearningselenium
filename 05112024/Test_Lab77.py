#Handle iframe- using Name or ID

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_02_iframe():
    driver = webdriver.Chrome()
    driver.get("https://demo.automationtesting.in/Frames.html")
    driver.maximize_window()
    time.sleep(3)

    # Switch to iframe using name or ID
    driver.switch_to.frame("singleframe")  # Name of the iframe

    # Interact with an element inside the iframe
    text_box = driver.find_element(By.XPATH, "//input[@type='text']")
    text_box.send_keys("Hello, Iframe!")

    # Switch back to main content
    driver.switch_to.default_content() # moves back to the main page

    driver.quit()
