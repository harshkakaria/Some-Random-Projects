from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as wait

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://10fastfingers.com/typing-test/english")

wait(5)

for i in range(0,1000):
	word = driver.find_element_by_class_name("highlight").text	
	driver.find_element_by_class_name("form-control").send_keys(word)
	driver.find_element_by_class_name("form-control").send_keys(u'\ue00d')




