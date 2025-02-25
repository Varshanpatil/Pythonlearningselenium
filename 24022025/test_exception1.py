import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    # NosuchElementexception
    try:
        element = driver.find_element(By.ID, "this_id_doesn't exist")

    except NoSuchElementException:
        print("Element not found!")

    print("End of the program")

