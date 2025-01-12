#Write a program on below test cases
#1.Open google on chrome browser 2. close or quit the browser 3. Again open Edge browser with facebook
#4.Print google

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
#driver.close()
driver.quit()

def test_sample():
    driver = webdriver.Edge()
    driver.get("https://facebook.com")
    print("Google")
    time.sleep(10)
test_sample()
