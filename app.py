from flask import Flask,render_template
from newsapi import NewsApiClient

app=Flask(__name__)

@app.route('/')
def index():