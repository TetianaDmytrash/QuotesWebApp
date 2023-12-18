"""
file with main GET, POST methods
"""
import json
from flask import Blueprint, redirect, url_for, flash, render_template, request, jsonify, make_response
from flask_login import login_user, login_required, logout_user, current_user
from passlib.hash import sha256_crypt

from app.database.database import session
from app.database.models import Author, Topic, Quote, User, UserQuote
from logs.logger import logger
from .validation_user import Validation

auth = Blueprint('auth', __name__)  # coincidence with the file name is not necessary


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    sign up user in system
    :return:
    """
    if request.method == 'POST':
        email = request.form.get('email')
        logger.warning('new user enter email: {}'.format(email))
        first_name = request.form.get('first_name')
        logger.warning('new user enter first Name: {}'.format(first_name))
        last_name = request.form.get('last_name')
        logger.warning('new user enter last Name: {}'.format(last_name))
        login = request.form.get('login')
        logger.warning('new user enter login: {}'.format(login))
        password_user = request.form.get('password_user')
        logger.warning('new user enter password: {}'.format(password_user))
        password_confirm = request.form.get('password_confirm')
        logger.warning('new user enter confirm password: {}'.format(password_confirm))

        user = session.query(User).filter_by(email=email).first()
        logger.warning('find user with same email: {}'.format(email))

        logger.warning('start validation info user')
        if Validation.validation_general(user,
                                         email,
                                         first_name,
                                         last_name,
                                         login,
                                         password_user,
                                         password_confirm):
            logger.warning('create new user')
            new_user = User(email=email,
                            first_name=first_name,
                            last_name=last_name,
                            login=login,
                            password=sha256_crypt.hash(password_user))
            session.add(new_user)
            logger.warning('add new user in database')
            session.commit()
            login_user(new_user, remember=True)
            logger.warning('login user')
            flash('Account created!', category='success')
            return redirect(url_for('view.profile'))
        else:
            return make_response(render_template('sign_up.html', user=current_user), 403)

    return render_template("sign_up.html", user=current_user)


# auth.route() - The decorator creates a link between the URL given as an argument and the function below.
@auth.route('/sign-in', methods=['GET', 'POST'])
def sign_in():
    """
    sign in user in system
    :return:
    """
    # request for data submitted in the form
    # data = request.form
    # render_template("sign_in.html", text="Testing", user="Tania") -
    # You can simply pass a variable separated by commas
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = session.query(User).filter_by(email=email).first()

        if user:
            if sha256_crypt.verify(password, user.password):
                # if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)  # remembers that he came in
                return redirect(url_for('view.profile'))
            else:
                flash('Incorrect email or password, try again.', category='error')
                return make_response(render_template('sign_in.html', user=current_user), 403)
        else:
            flash('Incorrect email or password, try again.', category='error')
            return make_response(render_template('sign_in.html', user=current_user), 403)
    else:
        return render_template("sign_in.html", user=current_user)


@auth.route('/sign-out')
@login_required
def sign_out():
    """
    sing out user from system
    :return:
    """
    logout_user()
    return redirect(url_for('view.start_page'))


@auth.route('/add-quote', methods=['GET', 'POST'])
@login_required
def add_quote():
    """
    add quote in profile user
    can do it only if he/she registered in system
    :return:
    """
    if request.method == "POST":
        quote = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
        quote_id = quote['quote_id']
        quote = session.query(Quote).get(quote_id)
        new_quote_user = UserQuote(quote_id=quote.id, user_id=current_user.id)
        session.add(new_quote_user)  # adding the quote to the database
        session.commit()
        flash('quote added to favorite!', category='success')
        return jsonify({})
    else:
        return redirect(url_for('auth.favorite'))


@auth.route('/delete-quote', methods=['POST'])
@login_required
def delete_quote():
    """
    delete quote in profile user
    can do it only if he/she registered in system
    :return:
    """
    quote = json.loads(request.data)  # this function expects a JSON from the INDEX.js file
    quote_id = quote['quote_id']
    quote = session.query(UserQuote).get(quote_id)
    if quote:
        if quote.user_id == current_user.id:
            session.delete(quote)
            session.commit()
            flash('quote deleted!', category='success')

    return jsonify({})


@auth.route('/favorite', methods=['GET', 'POST'])
@login_required
def favorite():
    """
    add quote in favorite in profile user
    can do it only if he/she registered in system
    :return:
    """
    if request.method == 'POST':
        quote = request.form.get('quote')  # Gets the quote from the HTML
        author_form = request.form.get('author')
        topic_form = request.form.get('topic')

        # print(quote)
        if len(quote) < 1 or len(author_form) < 1 or len(topic_form) < 1:
            flash('something went wrong.', category='error')
            return make_response(render_template('favorite.html', user=current_user), 403)
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

            new_quote_user = UserQuote(quote_id=new_quote.id, user_id=current_user.id)
            session.add(new_quote_user)  # adding the quote to the database
            session.commit()

            flash('quote added!', category='success')

    return render_template("favorite.html", user=current_user)
