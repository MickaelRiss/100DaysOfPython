import datetime as dt
import os
import random
import pandas as pd
import smtplib

MY_EMAIL = 'mickaelriss6@gmail.com'
MY_PASSWORD = "brgj bnnf lwps xkcc"

# Get current day and month
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Store birthdays in dict
data = pd.read_csv("birthdays.csv")
birthdays = {
    (row["month"], row["day"]): row
    for index, row in data.iterrows()
}

# If someone birthday create letter
if (today_month, today_day) in birthdays:
    letter = random.choice(os.listdir("./letter_templates"))
    with open(f"./letter_templates/{letter}", "r") as file:
        birthday_person = birthdays[(today_month, today_day)]
        new_letter = file.read()
        new_letter = new_letter.replace("[NAME]", birthday_person["name"])

# Send the letter generated
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{new_letter}"
        )
except Exception as e:
    print(f"It's not working becauuse of {e}")