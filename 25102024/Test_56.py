#Drag and drop action

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

def test_07_mouse():
    driver = webdriver.Chrome()
    driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
    driver.maximize_window()

    # Creating object for action
    action = ActionChains(driver)

    # Locate the source element and target element
    source_ele = driver.find_element(By.ID, "box6")
    target_ele = driver.find_element(By.ID, "box106")
    action.drag_and_drop(source_ele, target_ele).perform()  # drag and drop activity will done
    time.sleep(3)

    #Locate the element for seoul and south korea and drag seoul to and drop to south korea
    seoul = driver.find_element(By.ID, "box5")
    south_korea = driver.find_element(By.ID, "box105")
    action.drag_and_drop(seoul,south_korea).perform()
    time.sleep(3)