import urllib.request,json
from .models import Sources, News_Article

# Movie = movie.Movie
News_Articles = News_Article
# Getting api key
api_key = None

# Getting the news base url
base_url = None

article_url = None

def configure_request(app):
    global api_key,base_url, article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''

    get_sources_url =base_url.format(category,api_key)
    # print(get_movies_url)
    # print(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['results']:
            sources_results_list = get_sources_response['results']
            sources_results = process_results(sources_results_list)
    return sources_results
def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list : A list of dictionaries that contain source details

    Returns :
        source_results : A list of source objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')
        sources_object = Sources(id, name, description, url, category, country, language)
        sources_results.append(sources_object)

    return sources_results

def get_article(id):
    get_article_url = article_url.format(id, api_key)

    with urllib.request.urlopen(get_article_url) as url:
        article_results = json.loads(url.read())
        article_object = None
        # print(article_results)
        if article_results['results']:
            article_object = process_article(article_results['results'])

    return article_object

# def search_movie(movie_name):
#     search_movie_url = 'https://api.themoviedb.org/3/search/movie/?api_key={}&query={}'.format(api_key,movie_name)
#     with urllib.request.urlopen(search_movie_url) as url:
#         search_movie_data = url.read()
#         search_movie_response = json.loads(search_movie_data)
#
#         search_movie_results = None
#
#         if search_movie_response['results']:
#             search_movie_list = search_movie_response['results']
#             search_movie_results = process_results(search_movie_list)
#
#     return search_movie_results
