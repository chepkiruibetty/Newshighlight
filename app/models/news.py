class News:
    '''
    News class to define News Objects
    '''

    def __init__(self,name, description, url, category, language, country):
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country


class Articles:
    '''
    Articles class to define Articles Objects
    '''

    def __init__(self,author, title, description, url, urlToImage, publishedAt, content):
        self.id = id
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
©