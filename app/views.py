from flask import render_template
from app import app

@app.route('/news/<int:news_id>')
def news(news_id):
    '''
    Views news page function that returns the news articles page and its data
    '''
    return render_template('news.html',id = news_id, title = id )

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Online News Platform'
    return render_template('index.html',title = title)
