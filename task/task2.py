import datetime
from argparse import Action
from email.policy import default
from time import sleep
from tokenize import String

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

file = open("log.txt", "w")

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
# option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

def s():
    default
    sleep(1)

def set_up():
    '''gets url and maximizes window'''
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def login():
    '''enters correct name and password. And clicks to button login'''
    user_name = driver.find_element(By.XPATH,'//*[@id="user-name"]')
    user_name.send_keys('standard_user')
    file.write('Success write name\n')
    s()
    user_pass = driver.find_element(By.XPATH,'//*[@id="password"]')
    user_pass.send_keys('secret_sauce')
    file.write('Success write password\n')
    s()
    login_button = driver.find_element(By.XPATH,'//*[@id="login-button"]')
    login_button.click()
    file.write('Success login\n')
    s()

def choose_goods():
    '''adds goods to cart'''
    good1_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    good2_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bike-light"]')
    good3_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    good4_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    good5_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]')
    good6_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]')
    good = str(input("выберите товары от 1 до 6\n"))
    if "1" in good:
        good1_button.click()
    if "2" in good:
        good2_button.click()
    if "3" in good:
        good3_button.click()
    if "4" in good:
        good4_button.click()
    if "5" in good:
        good5_button.click()
    if "6" in good:
        good6_button.click()
    file.write('Success add good(s)\n')
    s()

def enter_to_the_cart():
    '''clicks to button cart'''
    cart_button = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a')
    cart_button.click()
    file.write('Success enter_to_the_cart\n')
    s()


def checkout():
    '''clicks button checkout. Enters first name, last name and code. After clicks button continue'''
    checkout_b = driver.find_element(By.XPATH, '//*[@id="checkout"]')
    checkout_b.click()
    file.write('Success checkout\n')
    s()
    first_name = driver.find_element(By.XPATH,'//*[@id="first-name"]')
    first_name.send_keys(str(input("видите имя\n")))
    file.write('Success write first name\n')
    s()
    last_name = driver.find_element(By.XPATH,'//*[@id="last-name"]')
    last_name.send_keys(str(input("видите фамилию\n")))
    file.write('Success write last name\n')
    s()
    zip_or_code = driver.find_element(By.XPATH,'//*[@id="postal-code"]')
    zip_or_code.send_keys(str(input("видите код\n")))
    file.write('Success write code\n')
    s()
    continue_button = driver.find_element(By.XPATH, '//*[@id="continue"]')
    continue_button.click()
    file.write('Success continue\n')
    cancel_element = driver.find_element(By.XPATH,'//*[@id="cancel"]')
    action = ActionChains(driver)
    action.move_to_element(cancel_element).perform()
    driver.save_screenshot(f"screenshot of receipt\\screenshot_of_receipt"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")
    s()

def finish():
    '''clicks button finish'''
    finish_button = driver.find_element(By.XPATH,'//*[@id="finish"]')
    finish_button.click()
    file.write('Success finish\n')
    s()

def back_home():
    '''clicks button back home'''
    back_home_button = driver.find_element(By.XPATH,'//*[@id="back-to-products"]')
    back_home_button.click()
    file.write('Success back home\n')
    s()

def logout():
    '''clicks button menu and clicks button logout'''
    menu_b = driver.find_element(By.XPATH,'//*[@id="react-burger-menu-btn"]')
    menu_b.click()
    sleep(1)
    logout_button = driver.find_element(By.XPATH,'//*[@id="logout_sidebar_link"]')
    logout_button.click()
    file.write('Success logout\n')


def test_context_when_finished():
    '''checks context: Thank you for your order!'''
    correct_text = "Thank you for your order!"
    current_text = driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2')

    assert correct_text == current_text.text,'test_context_when_finished is failed'
    file.write("test_context_when_finished is ok\n")


def test_logout_redirect():
    '''checks that logouts correct and gets correct URL'''
    correct_url="https://www.saucedemo.com/"
    get_url=driver.current_url

    assert correct_url == get_url,"test_logout_redirect is failed"
    file.write("test_logout_redirect is ok\n")

set_up()

login()

choose_goods()

enter_to_the_cart()

checkout()

finish()
test_context_when_finished()

back_home()

logout()
test_logout_redirect()