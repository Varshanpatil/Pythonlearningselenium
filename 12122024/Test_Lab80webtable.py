#Handling webtable

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_01_webtable():
    driver = webdriver.Chrome()
    driver.get("https://testautomationpractice.blogspot.com/")
    driver.maximize_window()
    time.sleep(3)

    ele = driver.find_element(By.NAME,"BookTable")
    driver.execute_script("arguments[0].scrollIntoView();",ele)
    time.sleep(5)

    row = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr"))
    coloumnhead = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr/th"))
    coloumncell = len(driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr/td"))

    print(row)
    print(coloumnhead)
    print(coloumncell)
    print("BookName"+"     "+"Author"+"     "+"Subject"+"     "+"Price")

    for r in range(2,row+1):
        for c in range(1,coloumnhead+1):
            value=driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text

            print(value, end="     ")
    print()