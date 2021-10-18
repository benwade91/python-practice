from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class TwitterBot:
    def __init__(self, email, password, driver):
        self.email = email
        self.password = password
        self.login_url = 'https://twitter.com/i/flow/login'
        self.driver = driver

    def login(self):
        self.driver.get(self.login_url)
        time.sleep(10)
        email_input = self.driver.find_element(By.TAG_NAME, 'input')
        email_input.send_keys(self.email)
        email_input.send_keys(Keys.ENTER)
        time.sleep(5)
        username_input = self.driver.find_element(By.TAG_NAME, 'input')
        username_input.send_keys('Garbageman415')
        username_input.send_keys(Keys.ENTER)
        time.sleep(5)
        pw_input = self.driver.find_element(By.TAG_NAME, 'input')
        pw_input.send_keys(self.password)
        pw_input.send_keys(Keys.ENTER)

    def tweet(self, message):
        time.sleep(2)
        tweet_input = self.driver.find_element(By.XPATH, '//span[(text()="Tweet")]')
        tweet_input.click()
        time.sleep(2)
        self.driver.switch_to.active_element.send_keys(message)
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click()

