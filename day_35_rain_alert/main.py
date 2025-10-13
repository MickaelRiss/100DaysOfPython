import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

api_key = os.environ["API_KEY"]
OVM_Endpoint = os.environ["OVM_ENDPOINT"]

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

parameters = {
    "lat": 45.538921,
    "lon": -73.600273,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url=OVM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

# print(weather_data)
will_rain = False
for hour_data in weather_data["list"]:
    condition_code =  hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_="+12185795432",
        to="+14385436942",
    )
    print(message.status)