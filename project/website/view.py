from flask import Flask, render_template, Blueprint
from .database.database import session
from .database.models import Author, Topic, Quote
from flask_login import login_user, login_required, logout_user, current_user

view = Blueprint('view', __name__) # coincidence with the file name is not necessary

# Flask-маршрут для отображения данных
@view.route('/')
@view.route('/home')
def startPage():
	authors = session.query(Author).all()
	topics = session.query(Topic).all()
	quotes = session.query(Quote).all()
	return render_template('home.html', authors=authors, topics=topics, quotes=quotes, user=current_user)

#GET
@view.route('/quotes')
def quotes():
	quotes = session.query(Quote).all()
	return render_template('quoteTopic.html', quotes=quotes, user=current_user)

@view.route('/quoteTravel')
def quoteTravel():
	topicName = 'Travel'
	topic = session.query(Topic).filter_by(name=topicName).first()
	quotesForTopic = []
	if topic:
		quotesForTopic = topic.quotes
	else:
		ptint("no quotes this theme")
	return render_template("topics/quoteTravel.html", quoteTravel=quotesForTopic, user=current_user)

@view.route('/quoteLife')
def quoteLife():
	topicName = 'Life'
	topic = session.query(Topic).filter_by(name=topicName).first()
	quotesForTopic = []
	if topic:
		quotesForTopic = topic.quotes
	else:
		ptint("no quotes this theme")
	return render_template("topics/quoteLife.html", quoteLife=quotesForTopic, user=current_user)

@view.route('/quoteRace')
def quoteRace():
	topicName = 'Race'
	topic = session.query(Topic).filter_by(name=topicName).first()
	quotesForTopic = []
	if topic:
		quotesForTopic = topic.quotes
	else:
		ptint("no quotes this theme")
	return render_template("topics/quoteRace.html", quoteRace=quotesForTopic, user=current_user)

@view.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
	return render_template('profile.html', user=current_user)

