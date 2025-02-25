#Handle Autosuggestion in selenium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def test_02_autosuggestion():
    driver = webdriver.Chrome()
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    time.sleep(2)

    close_popup= driver.find_element(By.CLASS_NAME,"commonModal__close")
    close_popup.click()

    #Locate the Delhi webelemnt and type g & autosuggestion dropdown we can see
    delhi_element = driver.find_element(By.ID,"fromCity")
    delhi_element.click()

    from_element = driver.find_element(By.XPATH,"//input[@placeholder='From']")
    from_element.send_keys("g")
    time.sleep(3)

    #Creating object for actions class-need to down in the autosuggestion using keyboard actions 3 times and select gorkhapur
    actions =ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(5)

    driver.quit()





