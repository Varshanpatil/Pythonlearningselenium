
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test01_links():
    driver= webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()

    #click on link
    driver.find_elements(By.LINK_TEXT,"Digital documents").click()
    #driver.find_elements(By.PARTIAL_LINK_TEXT,"Digital")

    #Find the no of links in a page
    links = driver.find_elements(By.XPATH,'//a')
    #links= driver.find_elements(By.TAG_NAME,'//a')
    #print("Total no of links:", len(links))

    #print all the link name
    for link in links:
        print(link.text)

