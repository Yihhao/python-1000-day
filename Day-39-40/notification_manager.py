from twilio.rest import Client
import os
import smtplib

TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_VIRTUAL_NUMBER = os.environ.get("TWILIO_VIRTUAL_NUMBER")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")
MY_EMAIL = os.environ.get("Email")
MY_PASSWORD = os.environ.get("PASSWORD")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, send_message):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages \
            .create(
            body=send_message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=PHONE_NUMBER
        )

        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smth.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )

