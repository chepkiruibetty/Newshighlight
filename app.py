from flask import Flask,render_template
from newsapi import NewsApiClient

app=Flask(__name__)

@app.route('/')
def index():
    newsapi =NewsApiClient(api_key='NEWS_API_CLIENT')
    topheadlines  = newsapi.get_top_headlines(source="BBC news")
articles = topheadlines['articles']
desc =