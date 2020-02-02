import unittest
from models import news , articles
News = news.news

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('BBC','Driver charged for murder of four children','"http://www.bbc.co.uk/news','general','en','US')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_news.name,'name')
        self.assertEquals(self.new_news.description,'description')
        self.assertEquals(self.new_news.url,"url")
        self.assertEquals(self.new_news.category,'category')
        self.assertEquals(self.new_news.language,'language')
        self.assertEquals(self.new_news.category,'category')
        
        #articles test starts
        
Articles = articles.articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(self,author, title, description, url, urlToImage, publishedAt, content)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))
        
    def test_check_instance_variables(self):
        self.assertEquals(self.new_articles.author,'author')
        self.assertEquals(self.new_articles.title,'title')
        self.assertEquals(self.new_articles.description,"description")
        self.assertEquals(self.new_articles.url,'url')
        self.assertEquals(self.new_articles.urlToImage,'urlToImage')
        self.assertEquals(self.new_articles.publishedAt,'publishedAt')
        self.assertEquals(self.new_articles.content,'content')
        

if __name__ == '__main__':
    unittest.main()
