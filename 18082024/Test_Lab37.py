#WRT-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_03_JS3():
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_1cfjttkdmt_e&adgrpid=155259812393&hvpone=&hvptwo=&hvadid=728858856222&hvpos=&hvnetw=g&hvrand=15085611210711468778&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9040245&hvtargid=kwd-28878962&hydadcr=14456_2409553&gad_source=1")
    driver.maximize_window()

    #Click on Bestseller button present on Amazon homepage
    best_sellers = driver.find_element(By.LINK_TEXT,"Best Sellers")
    driver.execute_script("arguments[0].click();",best_sellers)

    #Want title of the webpage
    title = driver.execute_script("return document.title; ")
    print(title)

    #Refresh the page
   #driver.execute_script("history.go(0)")

   #Creating alert on the webpage
   # driver.execute_script("alert('Hello Varsha');")

    #Get all the text present on the webpage
  #  innner_text = driver.execute_script("return document.documentElement .innerText;")
  #  print(innner_text)

    #want to create red border around "best sellers" test present on amazon homepage
    #driver.execute_script("arguments[0].style.border = '3px solid red'",best_sellers)

    #scroll down to the botton of the page
    #driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #time.sleep(10)

    #Sreoll down till the specific element
   # sports_header = driver.find_element(By.XPATH,"//span[text()='Best Sellers in sports,Fitness & Outdoors']")
   # driver.execute_script("arguments[0].scrollIntoView(true);",sports_header)

    print(driver.execute_script("return navigate.userAgent;"))


