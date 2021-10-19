import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

# ---------- GATHER DATA FROM ZILLOW ---------------#
header = {
    "Accept-Encoding":"gzip, deflate",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "X-Forwarded-For": os.environ.get('IP'),
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get('https://www.zillow.com/phoenix-az/duplex/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Phoenix%2C%20AZ%22%2C%22mapBounds%22%3A%7B%22west%22%3A-112.48897261914063%2C%22east%22%3A-111.76112838085938%2C%22south%22%3A33.454308200492925%2C%22north%22%3A33.75740540999114%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A40326%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22price%22%3A%7B%22max%22%3A600000%7D%2C%22mp%22%3A%7B%22max%22%3A1457%7D%2C%22sf%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22apco%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D', headers=header)
zillow = response.text
soup = BeautifulSoup(zillow, 'html.parser')

properties = soup.find_all(class_='list-card-info')
properties_scraped = []

for lot in properties:
    try:
        address = lot.find(class_='list-card-addr')
        price = lot.find(class_='list-card-price')
        href = lot.find(class_='list-card-link')
        properties_scraped.append((address.text, price.text, href['href']))
    except:
        print(f"failed: properties[{properties.index(lot)}]")


# ---------- FORM SUBMIT FLOW ---------------#
chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(3)
driver.get('https://forms.gle/veFL8nWypFHtaxKw9')
driver.maximize_window()


def submit_property(address, price, url):
    fields = driver.find_elements(By.CLASS_NAME, 'quantumWizTextinputPaperinputInputArea')
    time.sleep(1)
    fields[0].click()
    time.sleep(1)
    driver.switch_to.active_element.send_keys(address)
    time.sleep(1)
    fields[1].click()
    time.sleep(1)
    driver.switch_to.active_element.send_keys(price)
    time.sleep(1)
    fields[2].click()
    time.sleep(1)
    driver.switch_to.active_element.send_keys(url)
    driver.find_element(By.XPATH, "//span[(text()='Submit')]").click()

    driver.find_element(By.XPATH, '//a[(text()="Submit another response")]').click()


for property_ in properties_scraped:
    submit_property(property_[0], property_[1], property_[2])
