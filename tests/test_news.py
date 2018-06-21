import unittest
from app.models import Sources

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.sources = Sources(1234,'The language of Databases','A look at how python is taking over the web','/khsjha27hbs.com','tech','en','U.S.A')

    def test_instance(self):
        self.assertTrue(isinstance(self.sources, Sources))
