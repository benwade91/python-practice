import smtplib
import time
import requests
import datetime
from secret_file import email, password, to_email, my_location


# --------------------MY DATA ------------------------ #

def sun_is_up():
    now = datetime.datetime.now().hour
    sun_data = requests.get(url=f"https://api.sunrise-sunset.org/json", params=my_location)
    sunrise = int(sun_data.json()['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(sun_data.json()['results']['sunset'].split('T')[1].split(':')[0])

    if sunrise <= now <= sunset:
        return True
    else:
        return False

# --------------------ISS DATA ------------------------ #


def iss_is_above():
    global iss_lat, iss_lng
    iss_data = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_lat = float(iss_data.json()['iss_position']['latitude'])
    iss_lng = float(iss_data.json()['iss_position']['longitude'])

    if my_location['lat']+5 >= iss_lat >= my_location['lat']-5:
        if my_location['lng']+5 >= iss_lng >= my_location['lng']-5:
            return True
    else:
        return False


while not sun_is_up():
    if iss_is_above():
        print('its up there')
        with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=to_email,
                msg=f"Subject:THE ISS IS VISIBLE!\n\n "
                    f"The International space station should be visible in the sky for a few more minutes!")

    else:
        print(iss_lat - my_location['lat'], iss_lng - my_location['lng'])
    time.sleep(10)

