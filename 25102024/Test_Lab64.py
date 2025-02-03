#wheel mouse action-vertically scroll in a web page using selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_01():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.apple.com/in")
    driver.maximize_window()
    time.sleep(5)


    # Create an ActionChains object
    actions = ActionChains(driver)
    actions.scroll_by_amount(0,2000).perform() #scrolls little down by 2000px
    time.sleep(3)
    actions.scroll_by_amount(0,-1500).perform()  #Scrolls little up by =1500px
    time.sleep(5)

    driver.quit()
