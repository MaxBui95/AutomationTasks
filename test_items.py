from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    def test_check_add_to_basket_button(browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        browser.implicitly_wait(7)
        add_to_basket_button=browser.find_element(By.CLASS_NAME,"btn-primary")
        time.sleep(5)
        assert add_to_basket_button.text is not None, "Add to busket button is not found"



finally:
    time.sleep(7)

