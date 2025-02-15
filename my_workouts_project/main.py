import os, requests

APP_ID = "2225448c"
API_KEY = os.getenv("API_KEY")

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
print(response.text)