import smtplib
import datetime as dt
import random
import pandas
import re
from secret_file import email, password, to_email

day = dt.datetime.now().day
month = dt.datetime.now().month
bd = pandas.read_csv('birthdays.csv')
name = None

for (index, row) in bd.iterrows():
    if row['month'] == month and row['day'] == day:
        name = row['name']

        with open(f'letter_templates/letter_{random.randint(1,3)}.txt') as letter_data:
            letter = re.sub("\\[NAME]", name, letter_data.read())

        with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=to_email,
                msg=f"Subject:Happy Birthday!\n\n {letter}")
