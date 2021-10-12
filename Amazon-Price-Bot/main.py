import os
from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.amazon.com/dp/B08C4LC7TG/ref=cm_sw_em_r_mt_dp_EK6PZQ3189HGD23KWPBR"
header = {
    "Accept-Encoding":"gzip, deflate",
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "X-Forwarded-For": os.environ.get('IP'),
    "Accept-Language": "en-US,en;q=0.9",
}
r = requests.get(url, headers=header).text
soup = BeautifulSoup(r, 'html.parser')

price = float(soup.find(id="priceblock_ourprice").text.replace("$", ""))
print(price)

if price < 420:
    with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
        connection.starttls()
        connection.login(user=os.environ.get('EMAIL_FROM'), password=os.environ.get('EMAIL_PASSWORD'))
        connection.sendmail(
            from_addr=os.environ.get('EMAIL_FROM'),
            to_addrs=os.environ.get('EMAIL_TO'),
            msg=f"Subject:Roomba Dealz!\n\n big deals on Roomba. \n {url}")
