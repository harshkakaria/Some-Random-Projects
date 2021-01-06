#import
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as wait

#init path
path = 'D:/TUT/Learn selenium/chromedriver.exe'

#init driver
driver = webdriver.Chrome(path)

#getting the website
driver.get("https://10fastfingers.com/typing-test/english")

wait(7)

#function to type 
def Typingbotmain():
    for i in range(0,1000):
    	word = driver.find_element_by_class_name("highlight").text	
    	driver.find_element_by_class_name("form-control").send_keys(word)
    	driver.find_element_by_class_name("form-control").send_keys(u'\ue00d')

#executig the commands
Typingbotmain()




