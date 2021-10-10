
import os
import requests
import datetime
from data_manager import DataManager

class FlightSearch:
    def __init__(self, kiwi, sheety):
        self.flights = []
        self.search_from = (datetime.datetime.now()+datetime.timedelta(days=14)).strftime('%d/%m/%Y')
        self.search_to = (datetime.datetime.now()+datetime.timedelta(days=20)).strftime('%d/%m/%Y')
        self.kiwi_endpoint = "https://tequila-api.kiwi.com/v2/search"
        self.kiwi_header = {'apikey': kiwi}
        self.flight_search = DataManager(sheety)
        self.populate_flights()

    def populate_flights(self):
        for search in self.flight_search.locations:
            kiwi_params = {
                'fly_from': 'SFO',
                'fly_to': search[1],
                'dateFrom': self.search_from,
                'dateTo': self.search_to,
                'oneForCity': 1,
                'partner_market': 'us',
                'limit': 1,
                'curr': 'USD'
            }
            response = requests.get(url=self.kiwi_endpoint, headers=self.kiwi_header, params=kiwi_params).json()['data']
            print(response)
            print(response[0]['route'][0]['airline'])
            print(response[0]['route'][0]['flight_no'])
            flight_date = response[0]['route'][0]['utc_departure'].split('T')[0]
            flight_to = response[0]['cityTo']
            flight_price = response[0]['price']
            if search[2] > flight_price:
                self.flights.append((flight_to, flight_date, flight_price))
