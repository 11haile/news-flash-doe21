# Import Flask
from flask import Flask, request, jsonify, render_template, redirect
import requests
import json
from api_wrapper import get_news
from settings import get_settings

settings = get_settings()

# Create an app instance
app = Flask(__name__)

# test

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

@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
