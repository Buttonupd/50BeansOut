class Source:
    '''
    Source class to define Source Objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country

class Top_headlines:
    '''
    Top_headlines class to define Top_headlines Objects
    '''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt = publishedAt
        self.content=content

class Article:
    '''
    Article class to define Article Objects
    '''
    def __init__(self,source,author,title,description,url,urlToImage,publishedAt,content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage= urlToImage
        self.publishedAt = publishedAt
        self.content=content
class Review:
    all_reviews = []

    def __init__(self, id, title,  urlToImage, review):
        self.news_id = news_id
        self.title = title
        self.urlToImage = urlToImage
        self.review = review

    @classmethod
    def get_reviews(cls, id):
        response = []

        for review in cls.all_reviews:
            if review.news_id == id:
                response.append(review)

        return response

    def save_review(self):
        Review.all_reviews.append(self)

    @classmethod
    def clear_reviews(cls):
        Review.all_reviews.clear()

    
