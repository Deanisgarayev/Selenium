from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

file = open('log.txt','w')
# driver = webdriver.Chrome()

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
# option.add_argument("--headless")
driver = webdriver.Chrome(options=option)

def check_drop_down():
    select = Select(driver.find_element(By.XPATH,'//*[@id="header_container"]/div[2]/div/span/select'))
    sleep(1)
    select.select_by_visible_text("Price (low to high)")

def move_to_element():
    action = ActionChains(driver)
    element = driver.find_element(By.XPATH,'//*[@id="page_wrapper"]/footer/div')
    action.move_to_element(element).perform()


def scroll():
    driver.execute_script("window, scrollTo(0,300);")


def check_backspace_and_select_all():
    set_up()
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    sleep(2)
    user_name.send_keys(Keys.BACKSPACE)
    file.write("Success backspace\n")
    user_name.send_keys(Keys.CONTROL + 'a')
    file.write("Success control a\n")

def refresh_page():
    driver.refresh()
    file.write("refreshed\n")

def set_up():
    driver.get('http://www.saucedemo.com/')
    driver.maximize_window()

def fake_login():
    user_name = driver.find_element(By.XPATH, '//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    # user_name.clear()
    file.write("Success write login\n")

    user_pass = driver.find_element(By.XPATH, '//input[@id="password"]')
    password = "secret_sauce1"
    user_pass.send_keys(password)
    file.write("Success write fake password\n")

    login_button = driver.find_element(By.XPATH, '//input[@id="login-button"]')
    login_button.click()
    file.write("Success clik button\n")

def logout():
    menu_button = driver.find_element(By.XPATH,'//*[@id="react-burger-menu-btn"]')
    menu_button.click()
    sleep(1)
    logout_button = driver.find_element(By.XPATH,'//*[@id="logout_sidebar_link"]')
    logout_button.click()
    file.write("Success logout\n")


def login():
    user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass = driver.find_element(By.XPATH,'//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)
    file.write("Success write password\n")

    login_button = driver.find_element(By.XPATH,'//input[@id="login-button"]')
    login_button.click()
    file.write("Success clik button\n")

def login_with_enter():
    user_name = driver.find_element(By.XPATH,'//input[@id="user-name"]')
    login = "standard_user"
    user_name.send_keys(login)
    file.write("Success write login\n")

    user_pass = driver.find_element(By.XPATH,'//input[@id="password"]')
    password = "secret_sauce"
    user_pass.send_keys(password)
    file.write("Success write password\n")

    user_pass.send_keys(Keys.ENTER)
    file.write("Success enter login\n")

def test_login_redirect():
    correct_url="https://www.saucedemo.com/inventory.html"
    get_url=driver.current_url

    assert correct_url == get_url,"test_login_redirect is failed"
    file.write("test_login_redirect is ok\n")

def test_context_after_login_is_correct():
    correct_text = "Products"
    current_text = driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/span')

    driver.save_screenshot(f"sc_real_login\\screenshot_test_context_after_login_is_correct_"
                           f"{datetime.datetime.now().strftime("%H.%M.%S-%Y.%m.%d")}.png")

    assert correct_text == current_text.text,"test_context_after_login_is_correct is failed"
    file.write("test_context_after_login_is_correct is ok\n")

def test_login_fake_label():
    correct_text = "Epic sadface: Username and password do not match any user in this service"
    current_text = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/div[3]/h3')

    assert correct_text == current_text.text,"test_login_fake_label is failed"
    file.write("test_login_fake_label is ok\n")

def test_logout_redirect():
    correct_url="https://www.saucedemo.com/"
    get_url=driver.current_url

    assert correct_url == get_url,"test_logout_redirect is failed"
    file.write("test_logout_redirect is ok\n")

def test_context_after_logout_is_correct():
    correct_text = "Accepted usernames are:"
    current_text = driver.find_element(By.XPATH, '//*[@id="login_credentials"]/h4')

    assert correct_text == current_text.text,"test_context_after_logout_is_correct is failed"
    file.write("test_context_after_logout_is_correct is ok\n")

def sc_real_login():
    set_up()
    login()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_real_login_with_enter():
    set_up()
    login_with_enter()
    test_login_redirect()
    test_context_after_login_is_correct()

def sc_fake_login():
    set_up()
    fake_login()
    test_login_fake_label()

def sc_logout():
    logout()
    test_logout_redirect()
    test_context_after_logout_is_correct()

# check_backspace_and_select_all()
# sc_fake_login()
sc_real_login()
# sc_real_login_with_enter()
# refresh_page()
# scroll()
# move_to_element()
# sc_logout()
check_drop_down()
file.close()


# Поиск локатора по индексу //div[@class="form_group"])[1]
# Поиск локатора по тексту //h4[contains(text(), 'Password for all')] or ‘//h4[text()='Password for all users:']
