import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    # StaleElementReferenceException
    try:
        textarea= driver.find_element(By.NAME, "q")
        driver.refresh()
        #Document HTML might change - refresh
        #element -texarea ->might be case that it is not avaiable now.
        #//Refresh,navigate othe rpage,change in the DOM elements (AJAX CALLS)-valueJS,Angular

        #try to fix the code
        textarea.send_keys("testing academy")
        print("End of the program")
        #staleelementreference
    except StaleElementReferenceException as see:
        print(see)
        print("Stale element reference")
        textarea = driver.find_element(By.NAME, "q")
        textarea.send_keys("testing academy")

