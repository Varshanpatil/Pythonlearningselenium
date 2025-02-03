#Example to handle action class-Need to pass caps on word "varsha patil" using keyboard events in firstname
#Keyboard events
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.action_chains import ActionChains

def test_01_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")

    #Navigate to the webelement for firtsname.,click it & send details
    firstname = driver.find_element(By.XPATH,"//input[@name='firstname']")
    firstname.click()
    #firstname.send_keys("varsha patil")

    #want to pass"VARSHA" in firstname using keyboard.If we press shift+keyboard button.It will type CAPS ON.
    #to do this activity we need to use actions class
    actions = ActionChains(driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(firstname,"varsha patil").key_up(Keys.SHIFT).perform()

    time.sleep(10)

    driver.quit()
