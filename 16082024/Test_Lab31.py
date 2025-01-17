#SVG Automation Problem - Find the Tripura and Click on It
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_shadow_root():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()

    states=driver.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in states:
        print(state.get_attribute("aria-label"))
        if "Maharashtra" in state.get_attribute("aria-label"):
            state.click()
            break

            time.sleep(10)


test_shadow_root()


#Not run