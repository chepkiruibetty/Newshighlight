from app import app
import urllib.request,json
from .models import News , Articles

News = news.News
Articles = article.Articles

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the News base url
base_url = app.config["NEWS_API_BASE_URL"]


def get_news(source):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url + api_key
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_movies_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if name:
            news_obj = News(id, name, description, url,
                            category, language, country)
            news_results.append(news_obj)
    return news_results

def get_articles(context):
    '''
    Function that gets the json responce to our url request
    '''
    get_article_url = base_url + api_key
    
    with urllib.request.urlopen(get_article_url) as url:
        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        article_results = None

        if get_articles_response['results']:
            news_articles_list = get_articles_response['results']
            articles_results = process_results(articles_results_list)
            return articles_results
        
def process_results(articles_results_list):
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
    return articles_results


    

