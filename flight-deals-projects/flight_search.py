import requests, os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

CITIES_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
AMADEUS_API_KEY = os.environ["AMADEUS_API_KEY"]
AMADEUS_API_SECRET = os.environ["AMADEUS_API_SECRET"]
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"
OFFERS_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"



class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = AMADEUS_API_KEY
        self._api_secret = AMADEUS_API_SECRET
        self._token = self._get_new_token()

    def get_city_code(self, city_name):
        
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
        else:
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
    
    def get_offers(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": "2",
            "currencyCode": "MXN",
            "travelClass": "ECONOMY",
            "nonStop": "true",
            "max": "10",
        }
        headers = {"Authorization": f"Bearer {self._token}"}
        response = requests.get(url=OFFERS_ENDPOINT, params=query, headers=headers)

        # Check for errors
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
    
# search = FlightSearch()
# search.get_city_code("London")