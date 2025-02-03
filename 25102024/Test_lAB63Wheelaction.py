#Wheel mouse aqction

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.action_chains import ActionChains

def test_025_wheel():
    driver = webdriver.Chrome()
    driver.get("https://accounts.google.com")
    driver.maximize_window()
    time.sleep(5)

    #Locat ethe "English" webelement
    english = driver.find_element(By.XPATH,"//div[@class='VfPpkd-aPP78e']").click()
    time.sleep(3)

    #filipino_lang = driver.find_elements(By.LINK_TEXT,"Filipino")
    filipino_lang = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/c-wiz/footer/div/div/div/div[2]/ul/li[15]")
    time.sleep(3)

    #Create object for the actions class
    actions = ActionChains(driver)
    actions.scroll_to_element(filipino_lang).perform()
    time.sleep(3)

    driver.quit()
