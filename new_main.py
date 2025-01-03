from datetime import datetime, timedelta
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

file = open("logs.txt","w")

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
# option.add_argument("--headless")
driver = webdriver.Chrome(options=option)


def check_check_box():
    driver.get('http://demoqa.com/checkbox')
    driver.maximize_window()
    # main_list=driver.find_element(By.XPATH,'//*[@id="tree-node"]/div/button[1]')
    main_list=driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/span/button')
    main_list.click()
    home_check_box=driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[1]/span/label')
    home_check_box.click()
    home_check_box.is_selected()
    file.write("check_box is selected\n")
    sleep(1)
    home_check_box.click()
    driver.back()
    sleep(1)
    driver.forward()

def check_radio_button():
    driver.get('http://demoqa.com/radio-button')
    driver.maximize_window()
    sleep(1)
    yes_radio = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div/div[2]/div[2]/div[2]/label')
    yes_radio.click()
    yes_radio.is_selected()
    file.write("radio_button is selected\n")

def check_buttons():
    driver.get('https://demoqa.com/buttons')
    driver.maximize_window()
    sleep(1)
    double_click_button = driver.find_element(By.XPATH,'//*[@id="doubleClickBtn"]')
    right_click_button = driver.find_element(By.XPATH,'//*[@id="rightClickBtn"]')
    click_button = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/button')

    action = ActionChains(driver)
    action.double_click(double_click_button).perform()
    file.write('success double_click_button\n')
    action.context_click(right_click_button).perform()
    file.write('success right_click_button\n')
    click_button.click()
    file.write('success click_button\n')

    correct_context_after_double_click_button = 'You have done a double click'
    correct_context_after_right_click_button = 'You have done a right click'
    correct_context_after_click_button = 'You have done a dynamic click'

    current_context_after_double_click_button = driver.find_element(By.XPATH,'//*[@id="doubleClickMessage"]')
    current_context_after_right_click_button = driver.find_element(By.XPATH,'//*[@id="rightClickMessage"]')
    current_context_after_click_button = driver.find_element(By.XPATH,'//*[@id="dynamicClickMessage"]')

    assert correct_context_after_double_click_button == current_context_after_double_click_button.text,('context_'
                                                                                                   'after_double_click_'
                                                                                                   'button is failed')
    file.write('context_after_double_click_button is ok\n')

    assert correct_context_after_right_click_button == current_context_after_right_click_button.text,('context_'
                                                                                                   'after_right_click_'
                                                                                                   'button is failed')
    file.write('context_after_right_click_button is ok\n')

    assert correct_context_after_click_button == current_context_after_click_button.text,('context_after_click_button '
                                                                                          'is failed')
    file.write('context_after_click_button is ok\n')

def check_date_picker():
    driver.get('https://demoqa.com/date-picker')
    driver.maximize_window()
    sleep(1)
    input_date = driver.find_element(By.XPATH,'//*[@id="datePickerMonthYearInput"]')
    input_date.send_keys(Keys.CONTROL + 'a')
    input_date.send_keys(Keys.DELETE)
    sleep(1)
    current_date = datetime.now().strftime("%d.%m.%Y")
    input_date.send_keys(current_date)
    input_date.send_keys(Keys.ENTER)
    sleep(1)


    input_date.send_keys(Keys.CONTROL + 'a')
    input_date.send_keys(Keys.DELETE)
    sleep(1)
    add_days = current_date + timedelta(days=10)
    input_date.send_keys(add_days)

    input_date_and_time = driver.find_element(By.XPATH,'//*[@id="dateAndTimePickerInput"]')
    input_date_and_time.send_keys(Keys.CONTROL + 'a')
    input_date_and_time.send_keys(Keys.DELETE)
    sleep(1)
    # current_datetime = datetime.now().strftime("%d.%m.%Y-%H.%M")
    # input_date_and_time.send_keys(current_datetime)
    # sleep(1)
    select_month = driver.find_element(By.XPATH,'//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div/span[1]')
    select_month.click()
    select_month_number_name = driver.find_element(By.XPATH,'//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/div[7]')
    select_month_number_name.click()
    select_year = driver.find_element(By.XPATH,'//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div/span[1]')
    select_year.click()
    select_year_number= driver.find_element(By.XPATH,'//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div[2]/div[1]/div[11]')
    select_year_number.click()
    select_number= driver.find_element(By.XPATH,'//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div[6]')
    select_number.click()
    select_time= driver.find_element(By.XPATH,'//*[@id="dateAndTimePicker"]/div[2]/div[2]/div/div/div[3]/div[2]/div/ul/li[46]')
    select_time.click()




# check_check_box()
# check_radio_button()
# check_buttons()
check_date_picker()
file.close()