import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    #открываем сайт
    link="http://suninjuly.github.io/file_input.html"
    browser=webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
    browser.get(link)

    #заполняем поле Имя
    input1=browser.find_element(By.NAME,"firstname")
    input1.send_keys("maaaaaaax")


    #заполняем поле фамилия
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("siuuuuuu")

    #заполняем поле почта
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("siuuuuuu@mail.com")


    #загружаем файл 1.txt
    current_dir=os.path.abspath(os.path.dirname("file_loading.py")) #получаем текущее местоположение файла
    file_path=os.path.join(current_dir,"1.txt") #добавляем к пути имя файла(который добавляем)

    #находим кнопку загрузки
    loading=browser.find_element(By.ID,"file")
    loading.send_keys(file_path)

    #кнопка сабмит
    button=browser.find_element(By.CSS_SELECTOR,"button.btn").click()


finally:
    time.sleep(5)
    browser.quit()