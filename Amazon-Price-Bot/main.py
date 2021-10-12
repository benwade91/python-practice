import os
from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.amazon.com/dp/B08C4LC7TG/ref=cm_sw_em_r_mt_dp_EK6PZQ3189HGD23KWPBR"
header = {

}
r = requests.get(url, headers=header).text
soup = BeautifulSoup(r, 'html.parser')

price = float(soup.find(id="priceblock_ourprice").text.replace("$", ""))

if price < 420:
    with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
        connection.starttls()
        connection.login(user=os.environ.get('EMAIL_FROM'), password=os.environ.get('EMAIL_PASSWORD'))
        connection.sendmail(
            from_addr=os.environ.get('EMAIL_FROM'),
            to_addrs=os.environ.get('EMAIL_TO'),
            msg=f"Subject:Roomba Dealz!\n\n big deals on Roomba. \n {url}")
