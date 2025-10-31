import time
from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

for row in sheet_data:
    print(row["iataCode"])
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_dest_code(row["city"])
        time.sleep(2)
print(sheet_data)

data_manager.destination_data = sheet_data
data_manager.update_destinations()
