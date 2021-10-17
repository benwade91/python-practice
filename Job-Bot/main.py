import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(2)
# NAVIGATE TO LINKEDIN
driver.get('https://www.linkedin.com')
driver.maximize_window()

# LOG IN
email_input = driver.find_element(By.ID, 'session_key')
email_input.send_keys(os.environ.get('LINKED_EMAIL'))
pw_input = driver.find_element(By.ID, 'session_password')
pw_input.send_keys(os.environ.get('LINKED_PW'))
pw_input.send_keys(Keys.ENTER)
time.sleep(1)

# CLOSE MESSAGE WINDOW
close_msg = driver.find_element(By.XPATH, '/html/body/div[5]/aside/div[1]/header/section[2]/button[2]')
close_msg.click()
time.sleep(1)

# NAVIGATE TO JOBS
jobs = driver.find_element(By.ID, 'ember23')
jobs.click()

# ENTER JOB SEARCH PREFERENCES
job_search = driver.find_element(By.XPATH, '//*[@aria-label="Search by title, skill, or company"]')
job_search.send_keys('software developer')
job_location = driver.find_element(By.XPATH, '//*[@aria-label="City, state, or zip code"]')
job_location.send_keys('san francisco')
search = driver.find_element(By.CLASS_NAME, 'jobs-search-box__submit-button')
search.click()
time.sleep(2)

# FILTER AVAILABLE JOBS
easy_app = driver.find_element(By.XPATH, '//button[(text()="Easy Apply")]')
easy_app.click()
time.sleep(.5)
exp_level = driver.find_element(By.XPATH, '//button[(text()="All filters")]')
exp_level.click()
time.sleep(.5)
intern = driver.find_element(By.XPATH, '//span[(text()="Internship")]')
intern.click()
time.sleep(.5)
entry = driver.find_element(By.XPATH, '//span[(text()="Entry level")]')
entry.click()
time.sleep(.5)
show_results = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/div/button[2]/span')
show_results.click()
time.sleep(.5)

# ACCESS LIST OF AVAILABLE JOBS
job_list = driver.find_elements(By.XPATH, '//li[(text()="Apply easily")]')

for job in job_list:
    print(job.text)
    try:
        job.click()
    except StaleElementReferenceException:
        driver.find_element(By.XPATH, '//li[(text()="Apply easily")]').click()
    try:
        apply_now = WebDriverWait(driver=driver, timeout=10, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[(text()="Apply now")]')))
        apply_now.click()

        for _ in range(3):
            try:
                submit = WebDriverWait(driver=driver, timeout=10, ignored_exceptions=ignored_exceptions)\
                    .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[(text()="Submit application")]')))
                submit.click()
            except NoSuchElementException:
                next_page = WebDriverWait(driver=driver, timeout=10, ignored_exceptions=ignored_exceptions)\
                    .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[(text()="Next")]')))
                next_page.click()

        print('Application Successful')

    except NoSuchElementException:
        print('next')
        continue

