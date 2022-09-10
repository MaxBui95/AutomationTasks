from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link="http://SunInJuly.github.io/execute_script.html"
    browser=webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    browser.get(link)

    #ищем Х
    X=browser.find_element(By.ID,"input_value")
    x=X.text
    y=calc(x)
    #вводим ответ в поле
    field=browser.find_element(By.ID,"answer")
    field.send_keys(y)
    #выбираем чекбокс
    browser.find_element(By.CLASS_NAME,"form-check-input").click()

    #выбираем радиобаттон
    radio = browser.find_element(By.ID,"robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    #нажимаем сабмит кнопку
    submit=browser.find_element(By.TAG_NAME,"button").click()





finally:
    time.sleep(5)
    browser.quit()
