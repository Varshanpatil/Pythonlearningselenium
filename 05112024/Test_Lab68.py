#To find any webelemt location

from selenium import webdriver
from selenium.webdriver.common.by import By

def find_element_location():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/")  # Open the Selenium homepage
    driver.maximize_window()

    # Locate an element (e.g., 'Downloads' button)
    element = driver.find_element(By.LINK_TEXT, "Downloads")

    # Get the location of the element
    location = element.location
    print(f"Element Location: x = {location['x']}, y = {location['y']}")

    # Quit the browser
    driver.quit()

# Run the function
find_element_location()
