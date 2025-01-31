import requests
from config import FINHUB_API_KEY


def fetch_news(category):
    url = (
        f'https://finnhub.io/api/v1/news?category={category}&'
        f'token={FINHUB_API_KEY}'
    )
    response = requests.get(url)

    # Check the status code of the response
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return []

    news_data = response.json()

    # Extract relevant information from the JSON response
    news_items = []
    for item in news_data:
        news_item = {
            'title': item.get('headline', 'No title'),
            'description': item.get('summary', 'No description'),
            'url': item.get('url', '#'),
            'source': item.get('source', 'Unknown source'),
            'published_at': item.get('datetime', 'Unknown date')
        }
        news_items.append(news_item)

    return news_items
