import os
import requests

class DataManager:
    def __init__(self, auth):
        self.locations = []
        self.sheety_auth = auth
        self.populate_data()

    def populate_data(self):
        sheety_endpoint = 'https://api.sheety.co/bed2391b4b626481b6b70abde42aa10d/flightPrices/sheet1'
        header = {'Authorization': f'Bearer {self.sheety_auth}'}
        flight_data = requests.get(url=sheety_endpoint, headers=header).json()['sheet1']

        for x in flight_data:
            loc = (x['location'], x['airport'], x['lowPrice'])
            self.locations.append(loc)

