from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep as wait

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get('https://pokeflix.tv/movies')
