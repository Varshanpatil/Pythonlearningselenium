
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_02_checkbox():
    driver = webdriver.Chrome()
    driver.get("https://www.ironspider.ca/forms/checkradio.htm")
    driver.maximize_window()

    #Select specific single checkbox and click it
    #single_checkbox = driver.find_element(By.XPATH,"//input[@value='red']").click()

    #Need to do scroll down th epage till the element
    #driver.execute_script("arguments[].scrollIntoView(true);",single_checkbox)
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    # Select multiple checkbox at a time
    multiple_checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
    print(len(multiple_checkboxes))

    # Iterate through the checkbox elements
    for checkbox in multiple_checkboxes:
        # Check the checkbox if it is not already checked
        if not checkbox.is_selected():
            checkbox.click()
        time.sleep(10)