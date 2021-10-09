import os
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch(os.environ.get('KIWI_API'), os.environ.get('SHEETY_AUTH'))
notify = NotificationManager(flight_search.flights)


notify.print_information()

