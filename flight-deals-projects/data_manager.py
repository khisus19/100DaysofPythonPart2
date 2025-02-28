import requests, os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
SHEETY_BEARER = os.getenv('SHEETY_BEARER')

sheety_auth_header = {
    "Authorization": f"Bearer {SHEETY_BEARER}"
}

sheety_json = {}

response = requests.get(SHEETY_ENDPOINT, json=sheety_json, headers=sheety_auth_header)
data = response.json()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices = data["prices"]

    def update_row(self, body):
        response = requests.put(url=f"{SHEETY_ENDPOINT}/{body["price"]["id"]}", json=body, headers=sheety_auth_header)
        return response.json()
