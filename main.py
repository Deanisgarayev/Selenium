from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get('http://www.saucedemo.com/')
driver.maximize_window()

sleep(5)