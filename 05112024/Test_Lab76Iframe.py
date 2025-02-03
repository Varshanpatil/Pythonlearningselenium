#Handle iframe- handle by switching using index

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_01_iframe():
    driver = webdriver.Chrome()
    driver.get("https://www.tutorialspoint.com/selenium/practice/frames.php")
    driver.maximize_window()
    time.sleep(3)

    iframe= driver.find_elements(By.TAG_NAME,"iframe")
    total = len(iframe)
    print("Total no of iframe present: ", total)

    #switching to frame
    driver.switch_to.frame(0)
    time.sleep(3)
    iframe1 = driver.find_element(By.XPATH,"/html/body/div/header/div[2]/h1")
    frame = iframe1.text
    print(frame)
    driver.switch_to.default_content()
    verify = driver.find_element(By.XPATH,"//h1[normalize-space()='Frames']")
    Text = verify.text
    print(Text)

    driver.quit()

