#Write a program-1)Open chrome   2)Open website & take home page screenshot and save

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

def screenshot():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    driver.maximize_window()

    driver.get_screenshot_as_file("D:\\Varsha Pycharm Projects\\Pythonlearningseleniumprograms\\16082024\\Youtube1.jpg")
    driver.quit()

screenshot()
