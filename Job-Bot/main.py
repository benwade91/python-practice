from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get('https://www.linkedin.com')
driver.maximize_window()

email_input = driver.find_element(By.ID, 'session_key')
email_input.send_keys(os.environ.get('LINKED_EMAIL'))

pw_input = driver.find_element(By.ID, 'session_password')
pw_input.send_keys(os.environ.get('LINKED_PW'))
pw_input.send_keys(Keys.ENTER)
time.sleep(1)
close_msg = driver.find_element(By.XPATH, '/html/body/div[5]/aside/div[1]/header/section[2]/button[2]')
close_msg.click()
time.sleep(1)
jobs = driver.find_element(By.ID, 'ember23')
jobs.click()

job_search = driver.find_element(By.XPATH, '//*[@aria-label="Search by title, skill, or company"]')
job_search.send_keys('software developer')

job_location = driver.find_element(By.XPATH, '//*[@aria-label="City, state, or zip code"]')
job_location.send_keys('san francisco')

search = driver.find_element(By.CLASS_NAME, 'jobs-search-box__submit-button')
search.click()

time.sleep(2)

easy_app = driver.find_element(By.XPATH, '//button[(text()="Easy Apply")]')
easy_app.click()
time.sleep(1)
exp_level = driver.find_element(By.XPATH, '//button[(text()="All filters")]')
exp_level.click()
time.sleep(1)
intern = driver.find_element(By.XPATH, '//span[(text()="Internship")]')
intern.click()
time.sleep(1)
entry = driver.find_element(By.XPATH, '//span[(text()="Entry level")]')
entry.click()
time.sleep(1)
show_results = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/button[2]/span')
show_results.click()

