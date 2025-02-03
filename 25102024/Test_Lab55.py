#Drag and drop action

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def test_06_mouse():
    driver = webdriver.Chrome()
    driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    driver.maximize_window()

    #Locate the source element and target element
    source_ele = driver.find_element(By.ID,"box6")
    target_ele = driver.find_element(By.ID,"box106")

    #Creating object for action
    action = ActionChains(driver)
    action.drag_and_drop(source_ele,target_ele).perform()  #drag and drop activity will done
    time.sleep(5)

