from flask import Flask, render_template, Blueprint
from .database.database import session
from .database.models import Author, Topic, Quote

auth = Blueprint('auth', __name__) # coincidence with the file name is not necessary

# Flask-маршрут для отображения данных
@auth.route('/')
@auth.route('/home')
def startPage():
	authors = session.query(Author).all()
	topics = session.query(Topic).all()
	quotes = session.query(Quote).all()
	return render_template('index.html', authors=authors, topics=topics, quotes=quotes)

#GET
@auth.route('/quotes')
def quotes():
	quotes = session.query(Quote).all()
	return render_template('quoteTopic.html', quotes=quotes)