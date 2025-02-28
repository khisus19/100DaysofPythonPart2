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
        self._api_key = AMADEUS_API_KEY
        self._api_secret = AMADEUS_API_SECRET
        self._token = self._get_new_token()
        self.get_city_code("Paris")

    def get_city_code(self, city_name):
        
        print(f"Using this token to get destination {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url=CITIES_ENDPOINT,
            headers=headers,
            params=query
        )
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
    
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
        data = response.json()
        # New bearer token. Typically expires in 1799 seconds (30min)
        print(f"Your token is {data['access_token']}")
        print(f"Your token expires in {data['expires_in']} seconds")
        return data['access_token']
    
# search = FlightSearch()
# search.get_city_code("London")