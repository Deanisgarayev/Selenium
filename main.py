from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://www.saucedemo.com/')
driver.maximize_window()

user_name = driver.find_element(By.ID,"user-name")
login = "standard_user"
user_name.send_keys(login)

password = driver.find_element(By.ID,"password")
password_name = "secret_sauce"
password.send_keys(password_name)


sleep(5)

