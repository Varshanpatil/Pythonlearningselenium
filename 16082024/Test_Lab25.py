#Write a program to select Brazil country from country dropdown
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def country_side():
    driver = webdriver.Chrome()
    driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
    driver.maximize_window()

    #Navigate to the country dropdown
    country_element = driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
    time.sleep(3)

    #select country from country dropdown
    countrylist = driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
    print(len(countrylist))

    #need to select specific country among all options-need to use for loop
    for country in countrylist:
        if country.text== "Brazil":
            country.click()
            time.sleep(3)
            break

country_side()
