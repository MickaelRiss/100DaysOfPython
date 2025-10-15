import os
import requests
from datetime import date, timedelta
from twilio.rest import Client

CURRENCY = "USD"
CRYPTO = "BTC"
COMPANY_NAME = "Bitcoin"
STOCK_API_KEY = os.getenv("API_KEY_ALPHA_VANTAGE")
NEWS_API_KEY = os.getenv("API_KEY_NEWS")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

today_date = date.today()
yesterday_date = today_date - timedelta(days=1)

stock_params = {
    "function": "DIGITAL_CURRENCY_DAILY",
    "symbol": CRYPTO,
    "market": CURRENCY,
    "apikey": STOCK_API_KEY
}

news_params = {
    "q": COMPANY_NAME,
    "from": f"{today_date}&",
    "sortBy": "popularity&",
    "apiKey": NEWS_API_KEY
}

def calculate_percentage(current, previous):
    if previous == 0:
        return float('inf')
    return (abs(current - previous) / previous) * 100.0

def get_crypto_chart():
    response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
    response.raise_for_status()
    data = response.json()
    today_close = data["Time Series (Digital Currency Daily)"][str(today_date)]["4. close"]
    yesterday_close = data["Time Series (Digital Currency Daily)"][str(yesterday_date)]["4. close"]
    variation = calculate_percentage(float(today_close), float(yesterday_close))
    return variation

def get_news():
    response = requests.get(url="https://newsapi.org/v2/everything?", params=news_params)
    response.raise_for_status()
    articles = response.json()["articles"]
    three_articles = articles[:3]
    return three_articles

percentage_change = get_crypto_chart()

# if percentage_change > 5:
news = get_news()

if percentage_change > 0:
    sms_crypto_variation = f"{CRYPTO}: 🔺 {round(percentage_change)}"
else:
    sms_crypto_variation = f"{CRYPTO}: 🔻 {round(percentage_change)}"

formatted_articles = [f"{sms_crypto_variation}\nHeadline: {new["title"]}. \nBrief: {new["description"]}" for new in news]

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_="+12185795432",
        to="+14385436942",
    )

    print(message.body)
    print(message.status)