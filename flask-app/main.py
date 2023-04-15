# Import Flask
from flask import Flask, request, jsonify, render_template
import requests
import json
from newsapi import get_news

# Create an app instance
app = Flask(__name__)

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

@app.route('/index/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        q = request.form.get('q')
        from_date = request.form.get('from_date')
        data = get_news(q=q, from_date=from_date)
        return render_template('index.html', data=data, q=q, from_date=from_date)
    else:
        data = get_news()
        return render_template('index.html', data=data)

@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)

if __name__ == '__main__':
    app.run(debug=True)
