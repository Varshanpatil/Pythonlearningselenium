#Scenario 1 – Verify item can be added to Cart
#1. Open browser
#2. Navigate to ebay.com
#3. Search for ‘book’
#4. Click on the first book in the list
#5. In the item listing page, click on ‘Add to cart’
#6. verify the cart has been updated and displays the number of items in the cart as shown

#Need to install basic packages
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ebay_test():

    # Set up the Chromedriver WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Set up WebDriverWait
    wait = WebDriverWait(driver, 10)  # will Wait up to 10 seconds

    # Need to open ebay.com website using 'get'
    driver.get("https://www.ebay.com/")
    driver.maximize_window()

    # username = "varshanpatil109@gmail.com"
    # passowrd = "abcd@123"
    time.sleep(3)

    # Search for 'book'
    search_box = driver.find_element(By.ID, "gh-ac")
    search_box.send_keys("book")
    #search_box.click()
    search_box.send_keys(Keys.RETURN)
    time.sleep(10)

    # Click on the first book in the list
    first_book = driver.find_element(By.XPATH,"//*[@id='item57841b8566']/div/div[2]/a/div/span")
    first_book.click()
    time.sleep(5)

    # Need to switch window
    total_tab = len(driver.window_handles)
    print(total_tab)

    # Handle new window
    window_handles = driver.window_handles
    if len(window_handles) > 1:
        driver.switch_to.window(window_handles[1])

    #Click on ‘Add to cart’
    add_to_cart_button = driver.find_element(By.XPATH,"//span[@class='ux-call-to-action__text'and text()='Add to cart']")
    add_to_cart_button.click()
    time.sleep(10)

    #Verify cart has been updated
    cart_count = driver.find_element(By.XPATH,"//span[@aria-label='Your shopping cart contains 1 items']")
    cart_item_count = cart_count.text
    assert int(cart_item_count) > 0, "Cart is not updated!"
    print(f"Test Passed: Cart updated with {cart_item_count} item(s)")

    # Close the browser
    driver.quit()

ebay_test()