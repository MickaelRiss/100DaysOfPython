import datetime as dt
import smtplib
import random

MY_EMAIL = "XXX"
MY_PASSWORD = "XXX"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt", "r") as file:
            quotes = file.readlines()
            quote = random.choice(quotes)

    print(quote)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="XXXX",
                msg=f"Subject: Monday Motivation\n\n{quote}"
            )
    except Exception as e:
        print(f"It's not working becauuse of {e}")