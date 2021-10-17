import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException,\
    StaleElementReferenceException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(1)
# NAVIGATE TO LINKEDIN
driver.get('https://www.linkedin.com')
driver.maximize_window()

# LOG IN
email_input = driver.find_element(By.ID, 'session_key')
email_input.send_keys(os.environ.get('LINKED_EMAIL'))
pw_input = driver.find_element(By.ID, 'session_password')
pw_input.send_keys(os.environ.get('LINKED_PW'))
pw_input.send_keys(Keys.ENTER)

# CLOSE MESSAGE WINDOW
close_msg = driver.find_element(By.XPATH, '/html/body/div[5]/aside/div[1]/header/section[2]/button[2]')
close_msg.click()

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
job_list = [job.find_element(By.XPATH, './../../..') for job in job_list]

# HOPEFULLY AUTOMATES FORMS ...?
def fill_form():
    try:
        driver.find_element(By.XPATH, '//option[(text()="Male")]').click()
    except NoSuchElementException:
        print('No sex')
    try:
        driver.find_element(By.XPATH, '//option[(text()="White")]').click()
    except NoSuchElementException:
        print('No race')
    try:
        driver.find_element(By.XPATH, '//option[(text()="I am not a protected veteran")]').click()
    except NoSuchElementException:
        print('No veteran')
    try:
        driver.find_element(By.XPATH, '//option[(text()="Yes, I have a disability, or have a history/record of having a disability")]').click()
    except NoSuchElementException:
        print('No disability')
    try:
        label = driver.find_element(By.XPATH, '//span[(text()="Preferred First Name")]')
        label.find_element(By.XPATH, './../../div/div/input').send_keys('Ben')
    except NoSuchElementException:
        print('No Name')
    try:
        label = driver.find_element(By.XPATH, '//span[(text()="How did you hear about this job?")]')
        label.find_element(By.XPATH, './../../div/div/input').send_keys('LinkedIn')
    except NoSuchElementException:
        print('No how did you hear')
    try:
        label = driver.find_element(By.XPATH, '//span[(text()="City*")]')
        label.find_element(By.XPATH, './../../div/div/input').send_keys('Pleasant Hill, California, United States')
    except NoSuchElementException:
        print('No city')
    try:
        label = driver.find_element(By.XPATH, '//span[(text()="Are you a U.S. Citizen?")]')
        label.find_element(By.XPATH, './../../div/select/option[(text()="Yes")]').click()
    except NoSuchElementException:
        print('No citezen')


# RECURSIVELY NAVIGATES APPLICATION FORM
def app_submit():
    try:
        submit = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=ignored_exceptions) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[(text()="Submit application")]')))
        submit.click()
        print('Application Successful')
        try:
            WebDriverWait(driver=driver, timeout=2, ignored_exceptions=ignored_exceptions)\
                .until(expected_conditions.presence_of_element_located(
                 (By.XPATH, '/html/body/div[3]/div/div/button/li-icon/svg'))).click()
        except NoSuchElementException:
            print('no modal')

    except TimeoutException:
        try:
            next_page = WebDriverWait(driver=driver, timeout=4, ignored_exceptions=ignored_exceptions) \
                .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[(text()="Next")]')))
            next_page.click()

            fill_form()
        except TimeoutException:
            review = WebDriverWait(driver=driver, timeout=4, ignored_exceptions=ignored_exceptions) \
                .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[(text()="Review")]')))
            review.click()

        app_submit()


# LOOPS THROUGH CURRENTLY DISPLAYED JOBS
for job in job_list:

    try:
        job.click()

    except StaleElementReferenceException:
        driver.find_elements(By.XPATH, '//li[(text()="Apply easily")][4]/../..').click()
    except ElementClickInterceptedException:
        driver.find_elements(By.XPATH, '//li[(text()="Apply easily")][3]/../..').click()

    try:
        time.sleep(.5)
        apply_now = WebDriverWait(driver=driver, timeout=2, ignored_exceptions=NoSuchElementException) \
            .until(expected_conditions.presence_of_element_located((By.XPATH, '//span[(text()="Apply now")]')))
        apply_now.click()

        app_submit()

    except StaleElementReferenceException:
        print('stale element')
        continue

    except TimeoutException:
        print('timeout')
        continue


driver.quit()
