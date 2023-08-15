DATA_URL = "https://api.sheety.co/394268a21ee7d73262f788bfe7f1aa09/flightDeals/prices"
import requests
from pprint import pprint
class DataManager:
    def __init__(self):
        self.destination_data = {}
    def get_destination_data(self):
        response = requests.get(url=DATA_URL).json()
        self.destination_data = response["prices"]
        return self.destination_data
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{DATA_URL}/{city['id']}",
                json=new_data
            )
            print(response.text)
    #This class is responsible for talking to the Google Sheet