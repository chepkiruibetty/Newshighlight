from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)

@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="bbb081415b6b417eb5d3fbfe57199cf8")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    publAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        publAt.append(myarticles['publishedAt'])
        

    mylist = zip(news, desc, img,url,publAt)

    return render_template('index.html', context = mylist)
@app.route('/bbc')
def bbc():
    newsapi = NewsApiClient(api_key="bbb081415b6b417eb5d3fbfe57199cf8")
    topheadlines = newsapi.get_top_headlines(sources="bbc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    publAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        publAt.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img,url,publAt)


    return render_template('bbc.html', context = mylist)
    
@app.route('/fox')
def fox():
    newsapi = NewsApiClient(api_key="bbb081415b6b417eb5d3fbfe57199cf8")
    topheadlines = newsapi.get_top_headlines(sources="fox-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []
    url = []
    publAt = []

    for i in range(len(articles)):
        myarticles = articles[i]

        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
        url.append(myarticles['url'])
        publAt.append(myarticles['publishedAt'])

    mylist = zip(news, desc, img,url,publAt)


    return render_template('fox.html', context = mylist)
    
if __name__ == "__main__":
    app.run(debug=True)