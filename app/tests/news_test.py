import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News('CNN', 'The Wall Street Journal', 'Sumathi Reddy', 'Facts and Myths', 'describe', 'https://www.wsj.com/articles/pandemic-deepens-catholic-churchs-financial-crunch-from-vatican-to-parishes-1158773691', 'https://images.wsgi.net/im-179933/social','nything bruv', 'as so maybe' )

    def test_case(self):
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
   