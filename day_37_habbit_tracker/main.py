import requests
import os
from datetime import date

pixela_endpoint = "https://pixe.la/v1/users"
TOKEN = os.getenv("MY_TOKEN")
ID = "graph1"
today = date.today()
TODAY_DATE = today.strftime("%Y%m%d")

headers = {
    "X-USER-TOKEN": TOKEN
}

## CREATE USER
USERNAME = "mickael"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

## CREATE GRAPH
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": ID,
    "name": "Walking Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

## POST PIXEL
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

km = input("How many Km you walked today?")

pixel_params = {
    "date": TODAY_DATE,
    "quantity": km
}

# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

## UPDATE PIXEL
update_pixel_endpoint = f"{pixel_endpoint}/{TODAY_DATE}"
new_km = input("What is the new Km value?")

update_pixel_params = {
    "quantity": new_km
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
# print(response.text)

## DELETE PIXEL
response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)