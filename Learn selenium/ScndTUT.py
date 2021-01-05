#imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import stdiomask
from time import sleep as wait
#Init Path
Path = "D:/TUT/Learn selenium/chromedriver.exe"

#getting inputs and init driver
user_id = "harshkakaria"
passw = stdiomask.getpass(prompt="PW :")


driver = webdriver.Chrome(Path)

#getting the website
driver.get("https://www.chess.com/")

#clicking the login buttton
login_Button = driver.find_element_by_xpath('//*[@id="sb"]/div[2]/a[9]')
login_Button.click()


wait(2)

#writing the username
username_Input = driver.find_element_by_xpath('//*[@id="username"]')
username_Input.send_keys(user_id)


wait(2)

#writing the passw
passw_input = driver.find_element_by_xpath('//*[@id="password"]')
passw_input.send_keys(passw)

#clicking the login bttn
login_Button2 = driver.find_element_by_xpath('//*[@id="login"]')
login_Button2.click()

wait(10)

driver.quit()