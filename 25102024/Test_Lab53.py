#Double click action

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def test_04_mouse():

    # Step 1: Initialize the WebDriver
    driver = webdriver.Chrome()

    # Step 2: Navigate to the Google homepage
    driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
    driver.maximize_window()

    #Field 1& 2 under iframe.so we need to switch to inframe
    driver.switch_to.frame("iframeResult")

    #Locate the field 1
    field1 = driver.find_element(By.XPATH,"//input[@id='field1']")
    field1.clear()
    field1.send_keys("varsha")

    #Locate the "copy text" button
    copytext_button = driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")

    #Creating object for action class & double click the action
    action = ActionChains(driver)
    action.double_click(copytext_button).perform()

    #Quiting the browser
    driver.quit()