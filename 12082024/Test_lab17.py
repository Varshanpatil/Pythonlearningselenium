#Write a program to get the css value of the webpage,like color, font size,background color using CSS value property

from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Chrome()
# Make sure you have the appropriate driver installed
driver.get("https://www.google.com")

# Locate an element
element = driver.find_element(By.ID,"APjFqb")

# Get the CSS value of a specific property
color = element.value_of_css_property("color")
print(f"The color of the element is: {color}")

# Get the font size CSS property
font_size = element.value_of_css_property("font-size")
print(f"The font-size of the element is: {font_size}")

#Get the background coulur od the webpage
background_color = element.value_of_css_property("background-color")
print(f"The background color of the element is: {background_color}")

# Close the browser
driver.quit()