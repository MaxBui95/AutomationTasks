from selenium import webdriver
browser = webdriver.Chrome(executable_path="C:\\chromedriver\\chromedriver.exe")
browser.execute_script("alert('Robots at work');")