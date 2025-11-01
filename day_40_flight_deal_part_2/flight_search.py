import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_SEARCH_URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"

class FlightSearch:
    def __init__(self):
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._token = self.get_new_token()

    def get_new_token(self):
        headers = {
            "Content-type": "application/x-www-form-urlencoded"
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret
        }
        response = requests.post(url=TOKEN_URL, data=body, headers=headers)
        data = response.json()
        return data["access_token"]

    def get_dest_code(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        params = {
            "keyword": city_name
        }
        response = requests.get(url=CITY_SEARCH_URL, headers=headers, params=params)

        try:
            iata_code = response.json()["data"][0]["iataCode"]
            print(iata_code)
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not found"

        return iata_code

    def search_flight(self, origin, dest, from_time, to_time, currency_code):
        headers = { "Authorization": f"Bearer {self._token}" }
        params = {
            "originLocationCode": origin,
            "destinationLocationCode": dest,
            "departureDate": from_time,
            "returnDate": to_time,
            "nonStop": "true",
            "currencyCode": currency_code,
            "adults": 1,
            "max": 10
        }
        response = requests.get(url=FLIGHT_SEARCH_URL, headers=headers, params=params)

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            return None

        return response.json()