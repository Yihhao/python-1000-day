import os
import requests

SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
SHEET_USERS_ENDPOINT = os.environ.get("SHEET_USERS_ENDPOINT")
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = []
        self.customer_data = []

    def get_destination_data(self):
        response = requests.get(SHEETY_PRICES_ENDPOINT, auth=(USER_NAME, PASSWORD))
        response.raise_for_status()
        data = response.json()

        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode'],
                }
            }
            put_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            response = requests.put(put_endpoint, json=new_data, auth=(USER_NAME, PASSWORD))
            print(response.text)

    def update_price_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "lowestPrice": city["lowestPrice"],
                }
            }
            put_endpoint = f"{SHEETY_PRICES_ENDPOINT}/{city['id']}"
            response = requests.put(put_endpoint, json=new_data, auth=(USER_NAME, PASSWORD))
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = SHEET_USERS_ENDPOINT
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
