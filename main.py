from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
login = "standard_user"
user_name.send_keys(login)

password = driver.find_element(By.XPATH,'//input[@id="password"]')
password_name = "secret_sauce"
password.send_keys(password_name)


sleep(1000)

# Поиск локатора по индексу //div[@class="form_group"])[1]
# Поиск локатора по тексту //h4[contains(text(), 'Password for all')] or ‘//h4[text()='Password for all users:']
