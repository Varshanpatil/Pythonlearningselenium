import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_03_checkbox():
    driver = webdriver.Chrome()

    # Navigate to the web page containing checkboxes
    driver.get("http://example.com/page-with-checkboxes")
    time.sleep(3)

    # Find all checkbox elements using CSS selector
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    # Iterate through the checkbox elements
    for checkbox in checkboxes:
        # Check the checkbox if it is not already checked
        if not checkbox.is_selected():
            checkbox.click()

test_03_checkbox()