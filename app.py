from flask import Flask,render_template
from newsapi import NewsApiClient

app=Flask(__name__)

@app.route('/')
def index():
    newsapi =NewsApiClient(api_key='bbb081415b6b417eb5d3fbfe57199cf8')