import time
from selenium import webdriver

def test_globalsqa():
    driver = webdriver.Chrome()
    driver.get("https://www.globalsqa.com/demo-site/select-dropdown-menu/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()

def test_omayo():
    driver = webdriver.Chrome()
    driver.get("https://omayo.blogspot.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()

def test_tutorialninja():
    driver = webdriver.Chrome()
    driver.get("https://tutorialsninja.com/demo")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()

def test_selenium143():
    driver = webdriver.Chrome()
    driver.get("https://selenium143.blogspot.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()

def test_youtube():
    driver = webdriver.Chrome()
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.quit()