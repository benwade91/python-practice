from airline_data import airline_dic

class NotificationManager:
    def __init__(self, flights):
        self.flights = flights

    def print_information(self):
        for flight in self.flights:
            print(f"Theres's a flight to {flight[0]} on {flight[1]} for ${flight[2]} on {airline_dic[flight[3]]} {flight[4]}")
