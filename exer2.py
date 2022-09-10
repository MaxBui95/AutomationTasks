import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link="http://suninjuly.github.io/find_link_text"
a=str(math.ceil(math.pow(math.pi, math.e)*10000))
try:
    browser = webdriver.Chrome(executable_path='C:\\chromedriver\\chromedriver.exe')
    browser.get(link)
    link2 = browser.find_element(By.LINK_TEXT,a)
    link2.click()
    input1=browser.find_element(By.NAME, "first_name")
    input1.send_keys("Max")
    input2=browser.find_element(By.NAME,"last_name")
    input2.send_keys("Bui")
    input3=browser.find_element(By.CLASS_NAME,"city")
    input3.send_keys("Toronto")
    input4=browser.find_element(By.ID,"country")
    input4.send_keys("Canada")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(20)
    browser.quit()