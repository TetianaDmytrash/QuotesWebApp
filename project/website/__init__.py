import os
from project.logger import logger
from flask import Flask
from flask_login import LoginManager

from .database.isCreated import IS_CREATED
from .database.database import engine, session
from .database.models import Base, User
from .database.fillDatabase import fill_database

from .auth import auth
from .view import view


def create_app():
    logger.warning(f"create flask")
    app = Flask(__name__)

    app.secret_key = 'your_secret_key_here'

    if IS_CREATED:
        logger.warning("Database exists.")
    else:
        engineCurrent = engine

        logger.warning("Database does not exist.")

        logger.warning(f"clear database")
        # Database Cleanup
        Base.metadata.drop_all(engineCurrent)

        logger.warning(f"create tables in database")
        # Creating tables in the database
        Base.metadata.create_all(engineCurrent)

        logger.warning(f"fill database")
        # Filling the database
        fill_database()

    logger.warning(f"add bluepoint auth")
    app.register_blueprint(auth, url_prefix='/')

    logger.warning(f"add bluepoint view")
    app.register_blueprint(view, url_prefix='/')

    login_manager = LoginManager()
    login_manager.login_view = 'auth.signIn'
    login_manager.init_app(app)

    @login_manager.user_loader
    def loadUser(id):
        return session.query(User).get(int(id))

    return app
