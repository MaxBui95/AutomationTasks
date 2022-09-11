from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'https://suninjuly.github.io/math.html'
    browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    browser.get(link)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    input1=browser.find_element(By.ID,"answer")
    input1.send_keys(y)

    #ищем чекбокс и кликаем
    box=browser.find_element(By.ID,"robotCheckbox").click()

    #ищем радиобаттон и кликаем
    radio=browser.find_element(By.ID,"robotsRule").click()
    #ищем сабмит кнопку и кликаем
    submit=browser.find_element(By.CLASS_NAME,"btn-default").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
