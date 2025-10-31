import os
import requests
from dotenv import load_dotenv

load_dotenv()
TOKEN_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
CITY_SEARCH_URL = "https://test.api.amadeus.com/v1/reference-data/locations/cities"

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
        headers = {
            "Authorization": f"Bearer {self._token}"
        }
        params = {
            "keyword": city_name
        }
        response = requests.get(url=CITY_SEARCH_URL, headers=headers, params=params)
        data = response.json()
        iata_code = data["data"][0]["iataCode"]
        print(iata_code)
        return iata_code