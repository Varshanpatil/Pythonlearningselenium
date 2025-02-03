


import time
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_03_windows():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/analyze/osa/13/heatmaps/1?token=eyJhY2NvdW50X2lkIjo2NjY0MDAsImV4cGVyaW1lbnRfaWQiOjEzLCJjcmVhdGVkX29uIjoxNjcxMjA1MDUwLCJ0eXBlIjoiY2FtcGFpZ24iLCJ2ZXJzaW9uIjoxLCJoYXNoIjoiY2IwNzBiYTc5MDM1MDI2N2QxNTM5MTBhZDE1MGU1YTUiLCJzY29wZSI6IiIsImZybiI6ZmFsc2V9&isHttpsOnly=1")
    main_window_handle = driver.current_window_handle
    print("Before Click " + main_window_handle)
    driver.maximize_window()
    time.sleep(3)

    #Locate the control element & variation-Unable to locate single element for now
    list = driver.find_elements(By.CSS_SELECTOR,"[data-qa='danawobuqa']")
    #Control - control = list[0]
    #veriation

    #Locate variation-1 element
    variation = list[1]
    #Creating action class object and try to click on variation webelement
    action = ActionChains(driver)
    action.click(variation).perform()
    time.sleep(10)

    #After open variation->need to locate the webelement CLICKMAP and need to click on it
    #click_map = driver.find_element(By.CSS_SELECTOR,"[data-qa='liqokuxuba']")

    all_handles = driver.window_handles   #2
    for handle in all_handles:
        if handle != main_window_handle:
            driver.switch_to.window(handle)
            print(driver.title)
            driver.switch_to.frame("heatmap-iframe")
            clickmap = driver.find_element(By.CSS_SELECTOR, "[data-qa='liqokuxuba']")
            clickmap.click()
            time.sleep(20)
    time.sleep(5)

    driver.quit()