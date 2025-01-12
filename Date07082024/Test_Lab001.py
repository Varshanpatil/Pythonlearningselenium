import time
from selenium import webdriver
driver = webdriver.Chrome()
#open chrome & youtube back to back on same browser with same tab
driver.get("https://facebook.com")
driver.get("https://www.youtube.com/")



