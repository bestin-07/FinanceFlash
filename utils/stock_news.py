import requests
from config import ALPHA_VANTAGE_API_KEY


def fetch_stock_news():
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&apikey={ALPHA_VANTAGE_API_KEY}'
    response = requests.get(url)
    news_data = response.json()
    return news_data
