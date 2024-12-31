from selenium import webdriver
from selenium.webdriver.common.by import By

file = open("logs.txt","w")

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
# option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

def set_up():
    '''gets url and maximizes window'''
    driver.get('http://demoqa.com/checkbox')
    driver.maximize_window()

def open_check_box():
    # main_list=driver.find_element(By.XPATH,'//*[@id="tree-node"]/div/button[1]')
    main_list=driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button')
    main_list.click()
    home_check_box=driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/span/label')
    home_check_box.click()
    home_check_box.is_selected()
    file.write("check_box is selected\n")
    home_check_box.click()




set_up()
open_check_box()
driver.back()
driver.forward()
file.close()