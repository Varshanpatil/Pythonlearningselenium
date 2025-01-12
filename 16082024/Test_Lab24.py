import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def salesforce_login():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Navigate to the Salesforce trial signup page
    driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")

    try:
        # Wait for the dropdown to be visible
        wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
        job_title_dropdown = wait.until(EC.presence_of_element_located((By.ID, "UserTitle")))

        # Create a Select object for the dropdown
        select = Select(job_title_dropdown)

        # Select "IT Manager" by visible text
        select.select_by_visible_text("IT Manager")

        # Pause to observe the selection (optional)
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()

# Call the function to run the script
salesforce_login()
