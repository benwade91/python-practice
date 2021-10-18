import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from twitter_bot import TwitterBot

chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)

driver.get('https://www.speedtest.net/')
driver.maximize_window()

# --------START WEB SPEED ASSESSMENT
driver.find_element(By.CLASS_NAME, 'start-text').click()

time.sleep(0)

dwnld_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upld_speed = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span')
print(dwnld_speed.text)
print(upld_speed.text)

# ------CREATE TWITTER BOT AND SEND TWEET.
twitter_bot = TwitterBot(os.environ.get("TWITTER_EMAIL"), os.environ.get("TWITTER_PW"), driver)
twitter_bot.login()
time.sleep(3)

# ------THIS IS WHERE I'D TWEET @ COMCAST FOR MY SLOW INTERNET
twitter_bot.tweet(message='hey guys, whats the deal?')
