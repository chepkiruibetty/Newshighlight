from flask import Flask,render_template
from newsapi import NewsApiClient

app=Flask(__name__)

@app.route('/')
def index():
    newsapi =NewsApiClient(api_key='NEWS_API_CLIENT')
    topheadlines  = newsapi.get_top_headlines(source="BBC news")
articles = topheadlines['articles']

    description=[]
    news=[]
    image=[]

    for i in range(len(articles)):
        myarticles = [articles[i]]
        news.append(myarticles['title'])
        description.append(myarticles['description'])
        image.append(myarticles)['urlToImage']
    
    mylist=zip(news,description,image)
    
    return render_template('index.html',context = mylist)

if __name__== "__main__":
    app.run(debug=True)