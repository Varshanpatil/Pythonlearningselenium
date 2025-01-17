#Write a program for 1.Open chrome 2.Open google & click on search bar type-Youtube & search
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def svgmaps_test():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    driver.maximize_window()

    #Navigate to search icon bar
    search_icon = driver.find_element(By.NAME,"q")
    search_icon.send_keys("Youtube")

    #Navigate to search icon ans dearch youtube
    #search_list = driver.find_elements(By.XPATH, "//*[local-name()='svg']")
    search_list = driver.find_elements(By.XPATH,"//span[@class='QCzoEc z1asCe MZy1Rb']//*[name()='svg']")
    search_list[0].click()
    time.sleep(5)


svgmaps_test()

#Need to find solution.Not run