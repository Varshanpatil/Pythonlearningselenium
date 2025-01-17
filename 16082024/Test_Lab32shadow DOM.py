#Find the element for some text and neseted text which is under

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_shadow_root():
   # options = webdriver.ChromeOptions
   # options.add_experimental_option("detach",True)

    driver = webdriver.Chrome()
    driver.get("http://watir.com/examples/shadow_dom.html")
  #  driver.implicitly_wait(10)

    #There are some elements which we can not indentify using locators.It will not work.Because elements are present
    # in shadow root.Kind of this element we need to handle with different approcach as well as javascriptexecutor

    #Navigate to the element "some text"
    shadow_root = driver.find_element(By.CSS_SELECTOR,'[id="shadow_host"]').shadow_root
    shadow_text = shadow_root.find_element(By.XPATH, '//*[@id="shadow_content"]').text
    print(shadow_text)

   #Navigate to the nested text
   inner_shadow_root = shadow_root.find_element(By.CSS_SELECTOR, '[id="nested_shadow_host"]').shadow_root
   inner_shadow_text = inner_shadow_root.find_element(By.CSS_SELECTOR,'[id="nested_shadow_content"]').text
   print(inner_shadow_text)

test_shadow_root()


#Not run



