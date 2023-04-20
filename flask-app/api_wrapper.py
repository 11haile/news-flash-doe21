import os
import requests

from newsapi import NewsApiClient

url = 'https://newsapi.org/v2/everything?'

# newsapi = NewsApiClient(api_key='a15fbc057aa04e399b3b128a57406996')

# def get_news(q=None, from_date=None):
#     newsapi = NewsApiClient(api_key='a15fbc057aa04e399b3b128a57406996')

#     top_headlines = newsapi.get_top_headlines(language='en',
#                                           sort_by='relevancy',
#                                           page=1)

#     if top_headlines['status'] == 'ok':
#         return top_headlines
#     else:
#         raise Exception(f"Error fetching news: {top_headlines['status']}")



def get_news(q=None, from_date=None):
    payload = {
        'sortBy': 'popularity',
        'pageSize': 10,
        'apiKey': 'a15fbc057aa04e399b3b128a57406996'
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



