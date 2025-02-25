#Handle Autosuggestion in selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_03_autosuggestion():
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    time.sleep(2)

    newdelhi = driver.find_element(By.XPATH, "//p[@title='New Delhi']")
    newdelhi.click()

    from_element =driver.find_element(By.ID,"input-with-icon-adornment")
    from_element.send_keys("M")
    from_element.click()
    time.sleep(5)


    #Creating object for actions class-need to down in the autosuggestion using keyboard actions 3 times and select Madurai
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(10)

