from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


user_name = "samuel.j.korth-1@ou.edu"
user_pass = "testpass1"
driver = webdriver.Chrome("C:\\Users\\Sam\\Downloads\\chromedriver_win32\\chromedriver.exe")
def title_check_enter():
    driver.get("https://hudl.com/login")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")
    email.send_keys(user_name)
    password.send_keys(user_pass)
    password.send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(EC.title_contains("Home"))
    assert driver.title == "Home - Hudl", "Homepage title correct after login w/enter key"
driver.close()