from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = service)
driver.get('https://web.whatsapp.com/')

input ('Scan QR Code and press Enter...')

search_box = driver.find_element(By.XPATH , '//div[@contenteditable = "true"][@role = "textbox"]')

search_box.send_keys('StudBud')
time.sleep(2)

contact = driver.find_element(By.XPATH , '//span[@title = "StudBud"]')
contact.click()
time.sleep(1)

message_box = driver.find_elements(By.XPATH , '//div[@contenteditable = "true"][@role = "textbox"]')[-1]



message = 'Happy Birthday Sweetie!🎉🎂 ,\nGood N88!\nSweet Dreams;)'
message_box.send_keys(message)
message_box.send_keys('\n')
