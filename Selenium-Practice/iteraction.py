from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pprint import pprint
import time

chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, 'cookie')

time_end = time.time() + 15
while time.time() < time_end:
    money = int(driver.find_element(By.ID, 'money').text)
    store = driver.find_element(By.CSS_SELECTOR, '#store')
    store_items = store.find_elements(By.TAG_NAME, 'div b')
    store_items.reverse()
    for item in store_items:
        if item.is_displayed():
            price = int(item.text.replace(',', '').split(' - ')[-1])
            if money > price:
                item.click()
                break
    cookie_time = time.time() + 5
    while time.time() < cookie_time:
        cookie.click()


print(int(driver.find_element(By.ID, 'money').text))


driver.quit()
