import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class TestFields(unittest.TestCase):
    def test_fields1(self):
        try:
            #открываем сайт
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
            browser.get(link)

            # Находим и  заполняем обязательные поля
            input1=browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
            input1.send_keys("Massimo")
            input2=browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
            input2.send_keys("Makar")
            input3=browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
            input3.send_keys("max@makar.mail.ca")
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!",welcome_text)

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()


if __name__ == "__main__":
    unittest.main()