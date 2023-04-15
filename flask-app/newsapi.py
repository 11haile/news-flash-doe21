import requests
import os

def get_news(q=None, from_date=None):
    API_KEY = os.environ.get('NEWS_API_KEY') # Replace with your API key if not using environment variable
    url = 'https://newsapi.org/v2/everything'

    # Default parameters
    params = {
        'apiKey': API_KEY,
        'pageSize': 10,
        'sortBy': 'publishedAt',
        'language': 'en',
    }

    # Add query parameters based on user input
    if q:
        params['q'] = q
    if from_date:
        params['from'] = from_date

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching news: {response.status_code}")
