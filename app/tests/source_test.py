import unittest
from app.models import Source



class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up amethod that will run every test
        '''
        self.new_source=Source( "abc-news",
                    "ABC News",
                    "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
                    "https://abcnews.go.com",
                    "general",
                    "en",
                    "us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))   


if __name__ == '__main__':
    unittest.main()        