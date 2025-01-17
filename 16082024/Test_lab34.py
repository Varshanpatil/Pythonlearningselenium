#WRT program- Open following website and click on shopnow button.Need to find the lement which is
# present under shadow_root

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def test_02_shodowDOM():
    driver = webdriver.Chrome()
    driver.get('https://shop.polymer-project.org/')
    driver.maximize_window()
    time.sleep(2)

    #Navigate the shop button
    #javascript executor-Clcik on shop now-element present uder shadow_root->copy JS path & paste it here
    shopnow = driver.execute_script('return document.querySelector("body > shop-app").shadowRoot.querySelector("iron-pages > shop-home").shadowRoot.querySelector("div:nth-child(2) > shop-button > a")')
    driver.execute_script('arguments[0].click();',shopnow)
  #  driver.execute_script('arguments[0].setattribut("value","testing");' , shopnow)
    time.sleep(100)
    print('Ok')

test_02_shodowDOM()