import requests
import os
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("Auth_Token")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER")

params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}
## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(STOCK_ENDPOINT, params=params)
response.raise_for_status()

stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_closing_data = data_list[0]
yesterday_closing_prize = float(yesterday_closing_data["4. close"])
print(yesterday_closing_prize)

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_prize = float(day_before_yesterday_data["4. close"])
print(day_before_yesterday_closing_prize)

difference = yesterday_closing_prize - day_before_yesterday_closing_prize
up_down = None
if difference > 0:
    up_down = '🔺'
else:
    up_down = '🔻'

diff_percent = round(difference / yesterday_closing_prize * 100)

# STEP 2: https://newsapi.org/
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(diff_percent) > 1:
    print("Get News")
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()

    articles = news_response.json()["articles"]

    three_articles = articles[:3]

    # STEP 3: Use twilio.com/docs/sms/quickstart/python
    # to send a separate message with each article's title and description to your phone number.
    formatted_article = [
        f"{STOCK_NAME}: {up_down}{diff_percent} \nHeadline: {article['title']}\nBrief: {article['description']}"
        for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_article:
        message = client.messages \
            .create(
            body=article,
            from_='+14243471941',
            to=PHONE_NUMBER
        )

        print(message.status)

# TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
