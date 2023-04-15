import requests

API_KEY = 'a15fbc057aa04e399b3b128a57406996'
BASE_URL = 'https://newsapi.org/v2/everything?'

def get_news(q=None, from_date=None):
    payload = {
        'sortBy': 'popularity',
        'pageSize': 10,
        'apiKey': API_KEY
    }
    
    if q:
        payload['q'] = q

    if from_date:
        payload['from'] = from_date

    response = requests.get(BASE_URL, params=payload)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {'error': 'Error fetching news'}
