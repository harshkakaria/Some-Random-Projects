from selenium import webdriver
from time import sleep as wait
#Init Path
Path = "D:/TUT/Learn selenium/chromedriver.exe"

driver = webdriver.Chrome(Path)

driver.get("https://www.chess.com/")

print(driver.title)
wait(5)
driver.quit()