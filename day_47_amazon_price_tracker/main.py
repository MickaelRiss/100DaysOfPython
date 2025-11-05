import os
from dotenv import load_dotenv
import smtplib
from bs4 import BeautifulSoup
import requests

load_dotenv()
SMTP_ADDRESS=os.getenv("SMTP_ADDRESS")
EMAIL_ADDRESS=os.getenv("EMAIL_ADDRESS")
PASSWORD=os.getenv("GOOGLE_PASSWORD")
USER_AGENT=os.getenv("USER_AGENT")
ACCEPT_LANGUAGE=os.getenv("ACCEPT_LANGUAGE")

headers = {
    "Accept-Language": ACCEPT_LANGUAGE,
    "User-Agent": USER_AGENT
}

# Get website
# URL = input("Enter your Amazon product URL: ")
response = requests.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1", headers=headers)
response.raise_for_status()
website = response.text

# Scrap website
soup = BeautifulSoup(markup=website, features="html.parser")
price_tag = soup.find(name="span", class_="a-offscreen").get_text()
product_price = float(price_tag.split("$")[1])

RIGHT_PRICE = 70

if RIGHT_PRICE < product_price:
    try:
        with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
            connection.starttls()
            connection.login(user=EMAIL_ADDRESS, password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_ADDRESS,
                to_addrs="mendos.prod@gmail.com",
                msg=f"Subject: Happy Birthday!\n\nMail Test"
            )
    except Exception as e:
        print(f"It's not working becauuse of {e}")