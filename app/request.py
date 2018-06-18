from app import app
import urllib.request,json
from .models import news

News = news.News

#Getting api api
api_key = app.config['NEWS_API_KEY']


#Getting the news base url
base_url = app.config['MOVIE_API_BASE_URL']

def get_news(id):
    '''
    Function that gets the json response to our url request
    '''
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = none

        if news_details_response:
            id = news_details_response.get('id')
            name = news_details_response.get('name')
            description = news_details_response.get('description')
            url = news_details_response.get('url')
            category = news_details_response.get('category')
            language = news_details_response.get('language')
            country = news_details_response.get('country')


            news_object = News(id,name,description,url,category,language,country)
    return movie_object

def process_results(new_list):
    '''
    Function that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns:
    news_results:A list of news Objects
    '''
    news_results =[]
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if url:
            news_object = News(id,name,description,url,category,language,country)
            news_results.append(news_object)
    return news_results
