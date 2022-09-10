from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    link="http://suninjuly.github.io/alert_accept.html"
    browser=webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    browser.get(link)

    button=browser.find_element(By.CLASS_NAME,"btn,btn-primary").click()


    #выбираем окно confirm и нажимаем ок
    confirm=browser.switch_to.alert
    confirm.accept()


    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1=browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    submit=browser.find_element(By.CLASS_NAME,"btn-primary").click()

finally:
    time.sleep(10)
    browser.quit()