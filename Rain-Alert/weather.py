import requests
from twilio.rest import Client
from secret_file import api_key

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    'lat': 37.7599,
    'lon': -122.4148,
    'appid': api_key
}

data = requests.get(OWM_endpoint, params=params)

today_hourly = data.json()['hourly'][:12]


def weather_report():
    rain = False
    for (hour) in today_hourly:
        weather_id = hour['weather'][0]['id']
        if weather_id < 700:
            rain = True
    if rain:
        print("its gonna rain")
    else:
        print("no rain today")


weather_report()