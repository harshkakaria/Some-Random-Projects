from selenium import webdriver

def read_creds():
    user = passw = ""
    with open("C:/Users/harsh/Desktop/New Text Document.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip()
        passw = file[1].strip()

    return user, passw


url = 'https://www.gmail.com'
chrome_driver_location = 'C:\Program Files (x86)\chromedriver.exe'
gmail_username ,gmail_password =  read_creds()


driver = webdriver.Chrome(executable_path=chrome_driver_location)

driver.get(url)

driver.implicitly_wait(60)
driver.find_element_by_id('identifierId').send_keys(gmail_username)
driver.find_element_by_id('identifierNext').click()

driver.implicitly_wait(60)
driver.find_element_by_name('password').send_keys(gmail_password)
driver.find_element_by_id('passwordNext').click()