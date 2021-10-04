import os
import requests


tesla_data = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&interval=5min&apikey={os.environ.get('ALPHA_API_KEY')}").json()['Time Series (Daily)']
dates = list(tesla_data.keys())
price_change = float(tesla_data[dates[0]]['4. close']) - float(tesla_data[dates[1]]['4. close'])
percent_change = price_change / float(tesla_data[dates[0]]['4. close'])
if percent_change > 0:
    price_news = f"TSLA 🔺{round(percent_change, 1)}%"
elif percent_change < 0:
    price_news = f"TSLA 🔻{round(percent_change, 1)}%"


news_params = {
    'q': 'tesla',
    'from': '2021-9-04',
    'sortBy': 'popularity',
    'apiKey': os.environ.get('NEWS_API_KEY')
}
tesla_news = requests.get(f"https://newsapi.org/v2/everything", params=news_params).json()["articles"]

headline = tesla_news[0]["title"]
body = tesla_news[0]["description"]

print(f"{price_news}\nHeadline: {headline}\nBrief: {body}")
