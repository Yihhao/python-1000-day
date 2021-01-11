import requests
import smtplib
import time
import os
from datetime import datetime

MY_LAT = 24.813829
MY_LONG = 120.967484

MY_EMAIL = os.environ.get("Email")
MY_PASSWORD = os.environ.get("PASSWORD")


def is_iss_overhand():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    UTC_time_now = time_now.hour - 8
    if sunset <= UTC_time_now <= sunrise:
        return True


# TODO If the ISS is close to my current position
# TODO and it is currently dark
# TODO Then send me an email to tell me to look up.
# TODO BONUS: run the code every 60 seconds.
while True:
    if is_iss_overhand() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="zxas12584163@gmail.com",
                msg=f"Subject:Look up👆\n\nThe ISS is above you in th sky."
            )
    time.sleep(60)