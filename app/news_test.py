import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behavior of the Movie class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('abc-news', 'ABC News', 'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.' ,'http://abcnews.go.com', 'general', 'en', 'us')

    def test_instance(self):
        self.assertTrue(instance(self.new_movie,Movie))

if __name__=='__main__':
    unittest.main()
