from selenium import webdriver

chrome_driver_path = '/Users/benjaminwade/Desktop/python-practice/chromedriver'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://amazon.com')
