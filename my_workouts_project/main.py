import os, requests
import datetime as dt

APP_ID = "2225448c"
API_KEY = os.getenv("API_KEY")
SHEETY_BEARER_TOKEN = os.getenv("BEARER_TOKEN")

GENDER = "male"
WEIGHT_KG = "63"
HEIGHT_CM = "170"
AGE = "37"

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("How much did you exercise?: ")

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

data = {
    "query": exercise,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM
}

response = requests.post(url=API_ENDPOINT, json=data, headers=headers)
result = response.json()["exercises"][0]

## ------------- Posting in the sheet --------------- ##

SHEETY_ENDPOINT = "https://api.sheety.co/ce58ec8cd1cb64fb8e4754e155d62c2c/workoutTracking/workouts"

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

sheety_header = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

sheety_json = {
    "workout": {
        "date": today_date,
        "time": now_time,
        "exercise": result['user_input'].title(),
        "duration": result['duration_min'],
        "calories": result['nf_calories']
    }
}

response = requests.post(SHEETY_ENDPOINT, json=sheety_json, headers=sheety_header)
print(response.text)