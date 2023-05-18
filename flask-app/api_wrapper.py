import requests
from settings import get_settings

settings = get_settings()

url = 'https://newsapi.org/v2/everything?'

def get_news(q=None, from_date=None):
    payload = {
        'sortBy': 'popularity',
        'pageSize': 10,
        'apiKey': settings.api_key
    }
    
    if q:
        payload['q'] = q

    if from_date:
        payload['from'] = from_date

    response = requests.get(url, params=payload)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Error fetching news'}
