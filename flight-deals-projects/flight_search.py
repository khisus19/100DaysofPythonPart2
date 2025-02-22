import requests

BASE_URL = "https://test.api.amadeus.com/v1"
CITIES_ENDPOINT = "/reference-data/locations/cities"

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

headers = {
    "keywords": ""
}


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.get_city_code("Paris")

    def get_city_code(self, city):
        headers = {
            "keywords": city
        }
        # response = requests.get(url=f"{BASE_URL}{CITIES_ENDPOINT}", headers=headers)
        # print(response.text)
        # data = response.json()
        return "TESTING"
