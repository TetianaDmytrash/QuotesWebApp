"""
file with general config
"""
from logs.logger import logger
from flask import Flask
from flask_login import LoginManager

from app.database.is_created import IS_CREATED
from app.database.database import engine, session
from app.database.models import Base, User
from app.database.fill_database import fill_database

from app.auth import auth
from app.view import view


def create_app():
    """
    init file for project
    :return:
    """
    logger.warning('create flask')
    app = Flask(__name__)

    app.secret_key = 'your_secret_key_here'

    if IS_CREATED:
        logger.warning("Database exists.")
    else:
        engine_current = engine

        logger.warning("Database does not exist.")

        logger.warning("clear database")
        # Database Cleanup
        Base.metadata.drop_all(engine_current)

        logger.warning("create tables in database")
        # Creating tables in the database
        Base.metadata.create_all(engine_current)

        logger.warning("fill database")
        # Filling the database
        fill_database()

    logger.warning("add bluepoint auth")
    app.register_blueprint(auth, url_prefix='/')

    logger.warning("add bluepoint view")
    app.register_blueprint(view, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.signIn'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id_user):
        """
        :param id_user:
        :return:
        """
        return session.query(User).get(int(id_user))

    return app
