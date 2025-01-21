from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test03():
    # Open the demo page with radio buttons
    driver= webdriver.Chrome()
    driver.get("https://demo.guru99.com/test/radio.html")

    # Maximize the browser window
    driver.maximize_window()

    # Wait for the radio button to be visible (Explicit Wait)
    wait = WebDriverWait(driver, 10)
    radio_button = wait.until(EC.presence_of_element_located((By.ID, "vfb-7-3")))  # Option 3

    # Select the radio button if not already selected
    if not radio_button.is_selected():
        radio_button.click()
    print("Option 3 is selected.") 

    # Verify if the radio button is selected
    assert radio_button.is_selected(), "Radio button was not selected!"

    # Close the browser
    driver.quit()

