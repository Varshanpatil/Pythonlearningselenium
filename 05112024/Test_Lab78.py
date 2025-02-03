#Handling ifrmmae- handling nested iframe

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_02_iframe():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/nested_frames")
    driver.maximize_window()
    time.sleep(3)

    # Switch to parent iframe
    driver.switch_to.frame("frame-top")  #moves into the parent iframe.

    # Switch to child iframe inside the parent iframe
    driver.switch_to.frame("frame-left") #moves into the nested iframe.

    # Extract text inside nested iframe
    content = driver.find_element(By.TAG_NAME, "body").text
    print("Text inside nested iframe:", content)

    # Switch back to parent frame
    driver.switch_to.parent_frame()

    # Switch back to main content
    driver.switch_to.default_content()

    driver.quit()
