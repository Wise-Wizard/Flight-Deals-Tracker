import requests
from flight_data import FlightData
from dotenv import load_dotenv
import os
TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILA_ENDPOINT_V2 = "https://api.tequila.kiwi.com/v2"
load_dotenv(".env")
TEQUILA_API_KEY = os.getenv("TEQUILA_API_KEY")


class FlightSearch:
    def get_destination_code(self, city):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city, "location_types": "city"}
        response = requests.get(url=location_endpoint,
                                params=query, headers=headers)
        results = response.json()["locations"]
        return results[0]["code"]

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        location_endpoint = f"{TEQUILA_ENDPOINT_V2}/search"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "INR"
        }
        response = requests.get(url=location_endpoint,
                                headers=headers, params=query)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: INR {flight_data.price}")
        return flight_data
