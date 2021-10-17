from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('https://www.speedtest.net/')
driver.maximize_window()

# --------START WEB SPEED ASSESSMENT
driver.find_element(By.CLASS_NAME, 'start-text').click()

time.sleep(30)

dwnld_speed = driver.find_element(By.CLASS_NAME, 'download-speed')
upld_speed = driver.find_element(By.CLASS_NAME, 'upload-speed')
print(dwnld_speed.text)
print(upld_speed.text)


driver.quit()
