from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('https://www.python.org/')

event_list = driver.find_element(By.CLASS_NAME, 'event-widget')
line_items = event_list.find_elements(By.TAG_NAME, 'li')

event_dic = {}

for index, item in enumerate(line_items):
    time = item.find_element(By.TAG_NAME, 'time')
    location = item.find_element(By.TAG_NAME, 'a')
    event_dic[index] = {
            'time': time.text,
            'name': location.text
        }
print(event_dic)
driver.quit()
