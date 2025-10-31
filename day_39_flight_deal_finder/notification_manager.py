import os
from twilio.rest import Client

FROM_NUM = os.environ["TWILIO_FROM_NUM"]
TO_NUM = os.environ["TWILIO_TO_NUM"]

class NotificationManager:
    def __init__(self):
        self.client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    def send_message(self, price, origin, dest, from_date, to_date):
        message = self.client.messages.create(
            from_=FROM_NUM,
            to=TO_NUM,
            body=f"Low prices alert! Only £{price} to fly from {origin} to {dest} on {from_date} until {to_date}."
        )

        print(message.body)
        return message