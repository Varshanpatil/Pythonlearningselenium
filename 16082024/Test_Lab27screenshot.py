#Write a program-1)Open chrome   2)Open website & take home page screenshot and save

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def screenshot():
    driver = webdriver.Chrome()
    driver.get("https://demo.nopcommerce.com//")
    driver.maximize_window()

    #way-1
    driver.save_screenshot("D:\\Varsha Pycharm Projects\\Pythonlearningseleniumprograms\\16082024\\homepagess1.png")
    #way 2-we can import os module, then use .getcwd() command.No need to take full path from "D:\\to16082024"
    #Directly we can use -getscwd() and need to do concatinate with the filename of the screenshot which user want to give
    #Need to \\ double backslash in path
    driver.save_screenshot(os.getcwd()+"\\homepage2.png")
    driver.quit()

screenshot()

