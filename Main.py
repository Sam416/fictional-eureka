from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

blobs = open("blobs.txt")
user_name = blobs.readline()
user_pass = blobs.readline()
user_badpass = blobs.readline()
blobs.close()

driver = webdriver.Chrome()


def title_check_enter(user, passwd, expected_title):  # checks that the login works properly when enter is pressed
    driver.get("https://hudl.com/login")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    email.clear()
    email.send_keys(user)
    password.send_keys(passwd)
    password.send_keys(Keys.RETURN)
    WebDriverWait(driver, 5).until(EC.title_is(expected_title))
    assert driver.title == expected_title, f"Homepage title {driver.title} incorrect after login w/enter key"


def title_check_click(user, passwd, expected_title):
    # checks that the login works properly when the logIn button is clicked
    driver.get("https://hudl.com/login")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    login = driver.find_element_by_id("logIn")
    email.clear()
    email.send_keys(user)
    password.send_keys(passwd)
    login.click()
    WebDriverWait(driver, 5).until(EC.title_is(expected_title))  # wait until the title is what is expected or 5 seconds
    assert driver.title == expected_title, f"Homepage title {driver.title} incorrect after login w/ button click"


title_check_click(user_name, user_pass, "Home - Hudl")
title_check_enter(user_name, user_pass, "Home - Hudl")
title_check_click(user_name, user_badpass, "Log In - Hudl")
title_check_click(user_name, user_badpass, "Log In - Hudl")
driver.close()
