from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    #открываем сайт
    link="http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    browser.get(link)

    #ищем число №1 и число №2
    num1=browser.find_element(By.ID,"num1")
    num2=browser.find_element(By.ID,"num2")
    Num1=int(num1.text)
    Num2=int(num2.text)
    Sum=Num1+Num2
    Sum=str(Sum)


    #ищем ответ
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(Sum)  # ищем элемент с нашей суммой

    #жмем кнопку сабмит
    submit=browser.find_element(By.TAG_NAME,'button').click()




finally:
    time.sleep(10)
    browser.quit()