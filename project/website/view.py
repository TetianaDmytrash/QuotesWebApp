from flask import Flask, render_template, Blueprint
from .database.database import session
from .database.models import Author, Topic, Quote
from flask_login import login_user, login_required, logout_user, current_user

view = Blueprint('view', __name__)  # coincidence with the file name is not necessary


# Flask-маршрут для отображения данных
@view.route('/')
@view.route('/home')
def start_page():
    authors = session.query(Author).all()
    topics = session.query(Topic).all()
    quotes = session.query(Quote).all()
    return render_template('home.html',
                           authors=authors,
                           topics=topics,
                           quotes=quotes,
                           user=current_user)


# GET
@view.route('/quotes')
def quotes():
    quotes = session.query(Quote).all()
    return render_template('quoteTopic.html',
                           quotes=quotes,
                           user=current_user)


@view.route('/quote-travel')
def quote_travel():
    topic_name = 'Travel'
    topic = session.query(Topic).filter_by(name=topic_name).first()
    quotes_for_topic = []
    if topic:
        quotes_for_topic = topic.quotes
    else:
        print("no quotes this theme")
    return render_template("topics/quoteTravel.html",
                           quote_travel=quotes_for_topic,
                           user=current_user)


@view.route('/quote-life')
def quote_life():
    topic_name = 'Life'
    topic = session.query(Topic).filter_by(name=topic_name).first()
    quotes_for_topic = []
    if topic:
        quotes_for_topic = topic.quotes
    else:
        print("no quotes this theme")
    return render_template("topics/quoteLife.html",
                           quote_life=quotes_for_topic,
                           user=current_user)


@view.route('/quote-race')
def quote_race():
    topic_name = 'Race'
    topic = session.query(Topic).filter_by(name=topic_name).first()
    quotes_for_topic = []
    if topic:
        quotes_for_topic = topic.quotes
    else:
        print("no quotes this theme")
    return render_template("topics/quoteRace.html",
                           quote_race=quotes_for_topic,
                           user=current_user)


@view.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    return render_template('profile.html', user=current_user)
