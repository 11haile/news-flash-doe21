# Import Flask
from flask import Flask, request, jsonify, render_template
import requests
import json
# Create an app instance
app = Flask(__name__)

url = 'https://newsapi.org/v2/everything?'

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

@app.route('/form/', methods = ['POST', 'GET'])
def form():
    data = get_news()
    print(data)
    return render_template('form.html',data = data)

@app.route('/index/', methods = ['POST', 'GET'])
def index():
    data = get_news(q="tesla", from_date="2023-02-10")
    print(data)
    
    return render_template('index.html', data = data)
 
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
    
        return render_template('data.html',form_data = form_data)
 


# if __name__ == '__main__':
app.run(debug=True)
# @app.route('/api/news/blabla', methods=['GET'])
# def news():
#     q = request.args.get('q')
#     from_date = request.args.get('from_date')

#     if not q and not from_date:
#         return jsonify({'error': 'You must provide at least one query parameter (q or from_date)'})

#     if q and from_date:
#         return jsonify({'error': 'You cannot provide both q and from_date parameters'})

#     if q:
#         data = get_news(q=q)
#     else:
#         data = get_news(from_date=from_date)

#     return jsonify(data)

# if __name__ == '__main__':
#     app.run(debug=True)