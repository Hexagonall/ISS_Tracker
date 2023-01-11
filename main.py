import time
import requests
from datetime import datetime
import smtplib

MY_LAT =  # Your latitude
MY_LONG = # Your longitude
MY_EMAIL = # Your Email
PASSWORD = # Your Email's Password
while True:
    # run the code every 60 seconds.
    time.sleep(60)
    def is_iss_overhead():
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        # getting ISS long and lat
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        # compare own location and ISS location
        if MY_LONG+5 >= iss_longitude >= MY_LONG-5 and MY_LAT+5 >= iss_latitude >= MY_LAT-5:
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

        time_now = dt.datetime.now()
        current_hour = time_now.hour

        if current_hour>= sunset or current_hour <= sunrise:
            return True

    #If the ISS is close to my current position
    # and it is currently dark
    # Then send me an email to tell me to look up.

    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp-mail.outlook.com") as mail:
            mail.starttls()
            mail.login(user=MY_EMAIL,password=PASSWORD)
            mail.sendmail(from_addr=MY_EMAIL,
                            to_addrs=#Email which message to be sent,
                            msg="Subject:LOOK UP\n\nThe ISS is above you in the sky ")



