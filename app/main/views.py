from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources,get_headlines,search_source

from ..models import Source, Top_headlines, Article
from .forms import ReviewForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    #getting the general sources
    general_source=get_sources('general')
    health=get_sources('health')
    entertainment=get_sources('entertainment')
    sport=get_sources('sports')
    technology=get_sources('technology')
    title='www.60BeansOut.Com'
    search_source=request.args.get('source_query')

    if search_source:
        return redirect(url_for('main.search',source_name=search_source))

    else:
        return render_template('index.html',title=title, general=general_source, health=health, entertainment=entertainment, sport=sport, technology=technology)


@main.route('/articles/review/new<id>', methods=['GET', 'POST'])
def topNews(id):
    articles=get_headlines(id)
    source=id

    form = ReviewForm()
    articles = get_sources(id)
    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(articles.id,title, articles.image,review)
        new_review.save_review()
        return redirect(url_for('main.articles',id = articles.id ))

    title = f'{article.title} review'
    return render_template('new_review.html',title = title, source=source, review_form=form, articles=articles)



    '''
    View content page function that returns the news content page and its data
    '''
    
    
        


@main.route('/search/<source_name>')
def search(source_name):
    '''
    View function to display the search results
    '''
    source_name_list=source_name.split(' ')
    source_name_format='-'.join(source_name_list)
    searched_sources=search_source(source_name_format)
    title=f'search results for {source_name}'
    return render_template('search.html',sources=searched_sources ,title=title)

