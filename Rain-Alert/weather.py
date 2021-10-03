import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
params = {
    'lat': 37.7599,
    'lon': -122.4148,
    'appid': os.environ.get("OWM_API_KEY"),
    'exclude': 'current, minutely, daily'
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
        weather_info = "It's gonna rain today. ☔️"
    else:
        weather_info = "No rain today!"

    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(os.environ.get("ACC_SID"), os.environ.get("TWILIO_AUTH"), http_client=proxy_client)
    message = client.messages \
        .create(
            body=weather_info,
            from_=os.environ.get("TWILIO_NUM"),
            to=os.environ.get("MY_NUM")
        )
    print(message.status)


weather_report()