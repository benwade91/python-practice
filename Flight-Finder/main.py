#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os
import requests
import datetime

search_from = (datetime.datetime.now()+datetime.timedelta(days=14)).strftime('%d/%m/%Y')
search_to = (datetime.datetime.now()+datetime.timedelta(days=20)).strftime('%d/%m/%Y')

kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
kiwi_header = {'apikey': os.environ.get('KIWI_API')}
kiwi_params = {
    'fly_from': 'SFO',
    'fly_to': 'LAX',
    'dateFrom': search_from,
    'dateTo': search_to,
    'oneForCity': 1,
    'partner_market': 'us',
    'limit': 5
}
long_ep = f"https://tequila-api.kiwi.com/v2/search?fly_from={'SFO'}&fly_to={'LAX'}&dateFrom={'10/10/2021'}&dateTo={'20/10/2021'}&oneForCity=1"
response = requests.get(url=kiwi_endpoint, headers=kiwi_header, params=kiwi_params)
print(response.json()['data'][0]['price'])
print(response.json()['data'][0]['airlines'])


