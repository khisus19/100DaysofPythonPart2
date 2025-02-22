#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.prices
search = FlightSearch()

# Update sheet_data with IATA codes
for item in sheet_data:
    item["iataCode"] = search.get_city_code(item["city"])

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
print(sheet_data)