#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

from datetime import datetime, timedelta
import time

data_manager = DataManager()
sheet_data = data_manager.prices
flight_search = FlightSearch()

# Update sheet_data with IATA codes
for item in sheet_data:
    item["iataCode"] = flight_search.get_city_code(item["city"])

# Update rows in the Google Sheet
for city_dict in sheet_data:
    update_body = {
        "price": {
            "id": city_dict["id"],
            "city": city_dict["city"],
            "iataCode": city_dict["iataCode"],
            "lowestPrice": city_dict["lowestPrice"]
        }
    }
    data_manager.update_row(update_body)

# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.get_offers(
        "MEX",
        destination["iataCodeBackup"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination['city']}: ${cheapest_flight.price} MXN")
    # Slowing down requests to avoid rate limit
    time.sleep(2)