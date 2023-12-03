from flask import Blueprint, redirect, url_for, flash, render_template, request, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from passlib.hash import sha256_crypt
import json

from .database.database import session
from .database.models import Author, Topic, Quote, User, UserQuote
from logger import logger

auth = Blueprint('auth', __name__) # coincidence with the file name is not necessary

@auth.route('/signUp', methods=['GET', 'POST'])
def signUp():
	if request.method == 'POST':
		email = request.form.get('email')
		logger.warning(f'new user enter email: {email}')
		firstName = request.form.get('firstName')
		logger.warning(f'new user enter first Name: {firstName}')
		lastName = request.form.get('lastName')
		logger.warning(f'new user enter last Name: {lastName}')
		login = request.form.get('login')
		logger.warning(f'new user enter login: {login}')
		passwordUser = request.form.get('passwordUser')
		logger.warning(f'new user enter password: {passwordUser}')
		passwordConfirm = request.form.get('passwordConfirm')
		logger.warning(f'new user enter confirm password: {passwordConfirm}')
		
		user = session.query(User).filter_by(email=email).first()
		logger.warning(f'find user with same email: {email}')
		from .validationUser import Validation
		logger.warning(f'start validation info user')
		if Validation.validationGeneral(user, 
										email, 
										firstName, 
										lastName, 
										login, 
										passwordUser,
										passwordConfirm):
			logger.warning(f'create new user')
			newUser = User(email=email, 
				firstName=firstName, 
				lastName=lastName, 
				login=login, 
				password=sha256_crypt.hash(passwordUser))
			session.add(newUser)
			logger.warning(f'add new user in database')
			session.commit()
			login_user(newUser, remember=True)
			logger.warning(f'login user')
			flash('Account created!', category='success')
			return redirect(url_for('view.profile'))

	return render_template("signUp.html", user=current_user)


#auth.route() - декоратор создаёт связь между URL‑адресом, заданным в качестве аргумента, и функцией, которая написана ниже.
@auth.route('/signIn', methods=['GET', 'POST'])
def signIn():
	#запрос на данные, отправленные в форме
	#data = request.form
	#render_template("signIn.html", text="Testing", user="Tania") - просто через запятую можно передать переменную
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')

		user = session.query(User).filter_by(email=email).first()

		if user:
			if sha256_crypt.verify(password, user.password):
			#if check_password_hash(user.password, password):
				flash('Logged in successfully', category='success')
				login_user(user, remember=True) #запоминает, что вошел
				return redirect(url_for('view.profile'))
			else:
				flash('Incorrect password, try again.', category='error')
		else:
			flash('Email does not exist.', category='error')

	return render_template("signIn.html", user=current_user)

@auth.route('/signOut')
@login_required 
def signOut():
	logout_user()
	return redirect(url_for('view.startPage'))

@auth.route('/addQuote', methods=['GET','POST'])
@login_required
def addQuote():  
	quote = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
	print(f'geeeeeeeeeeeeeeeeeeee: {quote}')
	quoteId = quote['quoteId']
	quote = session.query(Quote).get(quoteId)
	print(f'geeeeeeeeeeeeeeeeeeee: {quote}')
	newQuoteUser = UserQuote(quoteId=quote.id, userId=current_user.id)
	session.add(newQuoteUser) #adding the quote to the database 
	session.commit()
	flash('quote added to favorite!', category='success')

	#redirect(url_for('auth.favorite'))
	return jsonify({})


@auth.route('/deleteQuote', methods=['POST'])
@login_required
def deleteQuote():  
	quote = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
	quoteId = quote['quoteId']
	quote = session.query(UserQuote).get(quoteId)
	if quote:
		if quote.userId == current_user.id:
			session.delete(quote)
			session.commit()
			flash('quote deleted!', category='success')

	return jsonify({})



@auth.route('/favorite', methods=['GET', 'POST'])
@login_required
def favorite():
	if request.method == 'POST': 
		quote = request.form.get('quote')#Gets the quote from the HTML 
		authorForm = request.form.get('author')
		topicForm = request.form.get('topic')
		
		print(quote)
		if len(quote) < 1:
			flash('quote is too short!', category='error') 
		else:
			topic = session.query(Topic).filter_by(name=topicForm).first()
			if not topic:
				newTopic = Topic(name=topicForm)
				session.add(newTopic) #adding the quote to the database 
				session.commit()
				topic = session.query(Topic).filter_by(name=topicForm).first()
			
			author = session.query(Author).filter_by(name=authorForm).first()
			if not author:
				newAutor = Author(name=authorForm)
				session.add(newAuthor) #adding the quote to the database 
				session.commit()
				author = session.query(Author).filter_by(name=authorForm).first()
			
			newQuote = Quote(text=quote, authorId=author.id, topicId=topic.id)  #providing the schema for the quote 
			session.add(newQuote) #adding the quote to the database 
			session.commit()
			newQuote = session.query(Quote).filter_by(text=quote).first()
			
			newQuoteUser = UserQuote(quoteId=newQuote.id, userId=current_user.id)
			session.add(newQuoteUser) #adding the quote to the database 
			session.commit()
			
			flash('quote added!', category='success')
	
	return render_template("favorite.html", user=current_user)
