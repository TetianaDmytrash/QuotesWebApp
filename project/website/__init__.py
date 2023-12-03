import os
from logger import logger

def create_app():
	print(F"print create app aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
	from flask import Flask
	logger.warning(f"create flask")
	app = Flask(__name__)

	app.secret_key = 'your_secret_key_here'

	from .database.isCreated import IS_CREATED

	if IS_CREATED:
		logger.warning("Database exists.")
	else:
		from .database.database import engine
		engineCurrent = engine

		logger.warning("Database does not exist.")

		from .database.models import Base
		logger.warning(f"clear database")
		# Database Cleanup
		Base.metadata.drop_all(engineCurrent)

		logger.warning(f"create tables in database")
		# Creating tables in the database
		Base.metadata.create_all(engineCurrent)

		from .database.fillDatabase import fillDatabase
		logger.warning(f"fill database")
		# Filling the database
		fillDatabase()

	from .auth import auth
	logger.warning(f"add bluepoint auth")
	app.register_blueprint(auth, url_prefix='/')

	from .view import view
	logger.warning(f"add bluepoint view")
	app.register_blueprint(view, url_prefix='/')

	from flask_login import LoginManager
	from .database.database import session
	from .database.models import User
	login_manager = LoginManager()
	login_manager.login_view = 'auth.signIn'
	login_manager.init_app(app)

	@login_manager.user_loader
	def loadUser(id):
		return session.query(User).get(int(id))

	return app