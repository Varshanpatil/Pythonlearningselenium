import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException

def test_exception():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")

    try:
        (WebDriverWait(driver=driver,timeout=10).until
         (EC.element_to_be_clickable((By.ID,"submit"))))
        print("End of the program")

    except TimeoutException as see:
        print(see)
        print("Timeoutexception Occured! , 10 seconds passed")

    finally:
        driver.quit()


