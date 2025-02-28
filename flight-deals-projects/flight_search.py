import requests, os
from dotenv import load_dotenv

load_dotenv()

CITIES_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

# headers = {
#     "originLocationCode": "MEX",
#     "destinationLocationCode": "ZIH",
#     "departureDate": "2025-04-02",
#     "returnDate": "2025-04-04",
#     "adults": "2",
#     "currencyCode": "MXN",
#     "children": "1",
#     "travelClass": "ECONOMY",
#     "nonStop": "true"
# }


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.get_city_code("Paris")
        self._api_key = AMADEUS_API_KEY
        self._api_secret = AMADEUS_API_SECRET
        self._token = self._get_new_token()

    def get_city_code(self, city):
        header = {
            "keywords": city
        }
        response = requests.get(url=CITIES_ENDPOINT, headers=header)
        print(response.text)
        # data = response.json()
        return "TESTING"
    
    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }
        response = requests.post(url=TOKEN_ENDPOINT, headers=header, data=body)

search = FlightSearch()
search.get_city_code("London")