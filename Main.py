from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user_name = input("Email: ")
user_pass = input("Password: ")
driver = webdriver.Chrome("C:\\Users\\Sam\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://hudl.com/login")
element = driver.find_element_by_id("email")
element.send_keys(user_name)
element = driver.find_element_by_id("password")
element.send_keys(Keys.RETURN)
