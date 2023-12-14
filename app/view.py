"""
file with addition GET, POST methods
"""
from flask import render_template, Blueprint
from app.database.database import session
from app.database.models import Author, Topic, Quote
from flask_login import login_required, current_user

view = Blueprint('view', __name__)  # coincidence with the file name is not necessary


# Flask-route to display data
@view.route('/')
@view.route('/home')
def start_page():
    """
    call start page
    shows whether information is in the database
    :return:
    """
    authors = session.query(Author).all()
    topics = session.query(Topic).all()
    quotes_all = session.query(Quote).all()
    return render_template('home.html',
                           authors=authors,
                           topics=topics,
                           quotes=quotes_all,
                           user=current_user)


# GET
@view.route('/quotes')
def quotes():
    """
    displays quotes on which topics are in the database
    :return:
    """
    quotes_topic = session.query(Quote).all()
    return render_template('quote_topic.html',
                           quotes=quotes_topic,
                           user=current_user)


@view.route('/quote-travel')
def quote_travel():
    """
    displaying travel quotes on the screen
    :return:
    """
    topic_name = 'Travel'
    topic = session.query(Topic).filter_by(name=topic_name).first()
    quotes_for_topic = []
    if topic:
        quotes_for_topic = topic.quotes
    else:
        print("no quotes this theme")
    return render_template("topics/quote_travel.html",
                           quote_travel=quotes_for_topic,
                           user=current_user)


@view.route('/quote-life')
def quote_life():
    """
    displaying life quotes on the screen
    :return:
    """
    topic_name = 'Life'
    topic = session.query(Topic).filter_by(name=topic_name).first()
    quotes_for_topic = []
    if topic:
        quotes_for_topic = topic.quotes
    else:
        print("no quotes this theme")
    return render_template("topics/quote_life.html",
                           quote_life=quotes_for_topic,
                           user=current_user)


@view.route('/quote-race')
def quote_race():
    """
    displaying race quotes on the screen
    :return:
    """
    topic_name = 'Race'
    topic = session.query(Topic).filter_by(name=topic_name).first()
    quotes_for_topic = []
    if topic:
        quotes_for_topic = topic.quotes
    else:
        print("no quotes this theme")
    return render_template("topics/quote_race.html",
                           quote_race=quotes_for_topic,
                           user=current_user)


@view.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    """
    displaying user profile on the screen
    :return:
    """
    return render_template('profile.html', user=current_user)
