import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "PAR"
CURRENCY = "EUR"

# Update Sheet
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_dest_code(row["city"])
        time.sleep(2)

data_manager.destination_data = sheet_data
data_manager.update_destinations()

# Search Flights
tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_month_from_today = (datetime.now() + timedelta(days=180)).strftime("%Y-%m-%d")

for dest in sheet_data:
    flights = flight_search.search_flight(
      origin=ORIGIN_CITY_IATA,
      dest=dest["iataCode"],
      from_time=tomorrow,
      to_time=six_month_from_today,
      currency_code=CURRENCY,
    )
    print(f"DESTINATION: {dest["iataCode"]}")
    cheapest_flight = find_cheapest_flight(flights)

    # Send Message
    notification_manager = NotificationManager()
    notification_manager.send_message(
        price=cheapest_flight.price,
        origin=cheapest_flight.origin_airport,
        dest= cheapest_flight.destination_airport,
        from_date= cheapest_flight.out_date,
        to_date= cheapest_flight.return_date
    )