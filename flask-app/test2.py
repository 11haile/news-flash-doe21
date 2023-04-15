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


@app.route('/form/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        q = request.form.get('q')
        from_date = request.form.get('from_date')
        data = get_news(q=q, from_date=from_date)
        return render_template('form.html', data=data, q=q, from_date=from_date)
    else:
        data = get_news()
        return render_template('form.html', data=data)


# @app.route('/form/', methods = ['POST'])
# def form_input():
#     variable = request.form['q', 'from_date']

#     return variable


@app.route('/index/', methods = ['POST', 'GET'])
def index():
    variable = request.form['q', 'from_date']
    
    data = get_news('form.html', data = data, q='q',from_date='from_date')
    # print(data)
    
    return render_template('index.html',variable, data = data)
 
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
    
        return render_template('data.html',form_data = form_data, data = data)
 


if __name__ == '__main__':
    app.run(debug=True)
