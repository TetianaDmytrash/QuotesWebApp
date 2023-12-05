from flask import Blueprint, redirect, url_for, flash, render_template, request, jsonify
from flask_login import login_user, login_required, logout_user, current_user
from passlib.hash import sha256_crypt
import json

from .database.database import session
from .database.models import Author, Topic, Quote, User, UserQuote
from project.logger import logger

auth = Blueprint('auth', __name__)  # coincidence with the file name is not necessary


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        logger.warning(f'new user enter email: {email}')
        first_name = request.form.get('first_name')
        logger.warning(f'new user enter first Name: {first_name}')
        last_name = request.form.get('last_name')
        logger.warning(f'new user enter last Name: {last_name}')
        login = request.form.get('login')
        logger.warning(f'new user enter login: {login}')
        password_user = request.form.get('password_user')
        logger.warning(f'new user enter password: {password_user}')
        password_confirm = request.form.get('password_confirm')
        logger.warning(f'new user enter confirm password: {password_confirm}')

        user = session.query(User).filter_by(email=email).first()
        logger.warning(f'find user with same email: {email}')
        from .validationUser import Validation
        logger.warning(f'start validation info user')
        if Validation.validation_general(user,
										 email,
										 first_name,
										 last_name,
										 login,
										 password_user,
										 password_confirm):
            logger.warning(f'create new user')
            new_user = User(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            login=login,
                            password=sha256_crypt.hash(password_user))
            session.add(new_user)
            logger.warning(f'add new user in database')
            session.commit()
            login_user(new_user, remember=True)
            logger.warning(f'login user')
            flash('Account created!', category='success')
            return redirect(url_for('view.profile'))

    return render_template("signUp.html", user=current_user)


# auth.route() - декоратор создаёт связь между URL‑адресом, заданным в качестве аргумента, и функцией, которая написана ниже.
@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    # запрос на данные, отправленные в форме
    # data = request.form
    # render_template("signIn.html", text="Testing", user="Tania") - просто через запятую можно передать переменную
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = session.query(User).filter_by(email=email).first()

        if user:
            if sha256_crypt.verify(password, user.password):
                # if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)  # запоминает, что вошел
                return redirect(url_for('view.profile'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("signIn.html", user=current_user)


@auth.route('/sign-out')
@login_required
def sign_out():
    logout_user()
    return redirect(url_for('view.start_page'))


@auth.route('/add-quote', methods=['GET', 'POST'])
@login_required
def add_quote():
    quote = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
    quote_id = quote['quote_id']
    quote = session.query(Quote).get(quote_id)
    new_quote_user = UserQuote(quote_id=quote.id, user_id=current_user.id)
    session.add(new_quote_user)  # adding the quote to the database
    session.commit()
    flash('quote added to favorite!', category='success')

    # redirect(url_for('auth.favorite'))
    return jsonify({})


@auth.route('/delete-quote', methods=['POST'])
@login_required
def delete_quote():
    quote = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
    quote_id = quote['quote_id']
    quote = session.query(UserQuote).get(quote_id)
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
        quote = request.form.get('quote')  # Gets the quote from the HTML
        author_form = request.form.get('author')
        topic_form = request.form.get('topic')

        print(quote)
        if len(quote) < 1:
            flash('quote is too short!', category='error')
        else:
            topic = session.query(Topic).filter_by(name=topic_form).first()
            if not topic:
                new_topic = Topic(name=topic_form)
                session.add(new_topic)  # adding the quote to the database
                session.commit()
                topic = session.query(Topic).filter_by(name=topic_form).first()

            author = session.query(Author).filter_by(name=author_form).first()
            if not author:
                new_author = Author(name=author_form)
                session.add(new_author)  # adding the quote to the database
                session.commit()
                author = session.query(Author).filter_by(name=author_form).first()

            new_quote = Quote(text=quote, author_id=author.id, topic_id=topic.id)  # providing the schema for the quote
            session.add(new_quote)  # adding the quote to the database
            session.commit()
            new_quote = session.query(Quote).filter_by(text=quote).first()

            newQuoteUser = UserQuote(quote_id=new_quote.id, user_id=current_user.id)
            session.add(newQuoteUser)  # adding the quote to the database
            session.commit()

            flash('quote added!', category='success')

    return render_template("favorite.html", user=current_user)
