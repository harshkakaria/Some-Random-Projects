from selenium import webdriver
path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://accounts.google.com')
