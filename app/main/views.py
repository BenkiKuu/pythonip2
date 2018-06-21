from flask import render_template
from . import main
from ..request import get_sources,get_article


# Review = review.Review

#Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #Getting popular movie
    sport_news = get_sources('sports')
    tech_news = get_sources('technology')
    gen_news = get_sources('general')
    title = 'NEWSREAL-Headlines and Breaking News'
    return render_template('index.html', title=title, sports=sport_news, technology=tech_news, general=gen_news)




@main.route('/source/<id>')
def articles(id):
    """
    View articles
    """
    article = get_article(id)
    print(article)
    title = f'NEWSREAL News ~ {id}'
    return render_template('article.html', title=title, article=article)
