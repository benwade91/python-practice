from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time

time_end = time.time() + .5

chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')
store = driver.find_element(By.CSS_SELECTOR, '#store')
store_items = store.find_elements(By.TAG_NAME, 'div b')
store_items.reverse()
# store_items = [item.get_dom_attribute('id') != 'buyElder Pledge' for (item) in store.find_elements(By.TAG_NAME, 'div')]

for item in store_items:
    try:
        print(int(''.join(item.text.split()[-1].split(','))))
    except:
        pass


while time.time() < time_end:
    cookie.click()
    money = int(driver.find_element(By.ID, 'money').text)
    print(money)

driver.quit()