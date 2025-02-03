#Keyboard actions
#1.Ctrl +A -select full word. 2.Ctrl+C copy the text  3. Tab-go to the next coloumn  4. Ctrl + V - paste it


import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_01_keyboard():
    driver = webdriver.Chrome()
    driver.get("https://text-compare.com/")
    driver.maximize_window()

    #Locate the webelement for textarea 1 and textarea 2
    textarea1 = driver.find_element(By.ID,"inputText1")
    textarea2 = driver.find_element(By.ID,"inputText2")

    #type "Welcome Home" to text area 1
    textarea1.send_keys("Welcome Home")

    #Creating object for action class
    action = ActionChains(driver)

    #input 1- Ctrl +A -select full word.
    action.key_down(Keys.CONTROL)
    action.send_keys("A")     #to pass laphabets we use send_keys(aplhabets)
    action.key_up(Keys.CONTROL)
    action.perform()
    time.sleep(5)
    #We can write like this way or like this way also
    #action.key_down(Keys.CONTROL).send_keys("A").key_up(Keys.CONTROL).perform()

    #input 1- Ctrl+C copy the text
    action.key_down(Keys.CONTROL).send_keys("C").key_up(Keys.CONTROL).perform()

    #Press TAB key
    action.send_keys(Keys.TAB).perform()

    #CTrl+ v-paste here in text area 2
    action.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
    time.sleep(5)
