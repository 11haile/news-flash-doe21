# Import Flask
from flask import Flask, request, jsonify, render_template, redirect
import requests
import json
from api_wrapper import get_news

# Create an app instance
app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/form/')

@app.route('/form/', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        q = request.form.get('q')
        from_date = request.form.get('from')
        data = get_news(q=q, from_date=from_date)
        if 'articles' in data:
            return render_template('index.html', articles=data['articles'], q=q, from_date=from_date)
        else:
            return render_template('index.html', articles=[], q=q, from_date=from_date)
    else:
        data = get_news()
        return render_template('form.html', articles=data)

@app.route('/index/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        q = request.form.get('q')
        from_date = request.form.get('from')
        data = get_news(q=q, from_date=from_date)
        if 'articles' in data:
            return render_template('index.html', articles=data['articles'], q=q, from_date=from_date)
        else:
            return render_template('index.html', articles=[], q=q, from_date=from_date)
    else:
        data = get_news()
        return render_template('index.html', articles=data)

# @app.route('/form/', methods=['POST', 'GET'])
# def form():
#     if request.method == 'POST':
#         q = request.form.get('q')
#         from_date = request.form.get('from_param')
#         data = get_news(q=q, from_date=from_date)
#         return render_template('index.html', articles=data, q=q, from_date=from_date)
#     else:
#         data = get_news()
#         return render_template('form.html', articles=data)
    
# # @app.route('/index', methods=['POST'])
# # def process_form():
# #     q = request.form.get('q')
# #     from_date = request.form.get('from_param')

# #     api_key = 'a15fbc057aa04e399b3b128a57406996'
# #     api_url = f'https://newsapi.org/v2/everything?q={q}&from={from_date}&sortBy=publishedAt&apiKey={api_key}'

# #     response = requests.get(api_url)
# #     data = response.json()
# #     articles = data['articles']

# #     return render_template('index.html', articles=data, q=q, from_date=from_date)



# @app.route('/index/', methods=['POST', 'GET'])
# def index():
#     if request.method == 'POST':
#         q = request.form.get('q')
#         from_date = request.form.get('from_param')
#         data = get_news(q=q, from_date=from_date)
#         return render_template('index.html', articles=data, q=q, from_date=from_date)
#     else:
#         data = get_news()
#         return render_template('index.html', articles=data)

@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
