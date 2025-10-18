import requests
import os
from datetime import datetime

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
GENDER = "MALE"
WEIGHT_KG = 64
HEIGHT_CM = 174
AGE = 27
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/8019fe59908391271e5d3ddcc72af8f4/myWorkout/workouts"
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

nutritionix_headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

query = input("Tell me what you did today: ")

params = {
    "query": query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, headers=nutritionix_headers, json=params)
response.raise_for_status()
data = response.json()["exercises"]

date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

sheety_headers = {
    "Authorization": SHEETY_AUTH
}

for exercise in data:
    params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, headers=sheety_headers, json=params)
    response.raise_for_status()
    print(response.text)