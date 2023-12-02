import os
from logger import logger

def create_app():

	from flask import Flask
	logger.warning(f"create flask")
	app = Flask(__name__)

	from .database.database import IS_CREATED, DB_NAME

	if IS_CREATED and DB_NAME == "sqlite:///dataBase.db":
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

	#from view import view
	#logger.warning(f"add bluepoint view")
	#app.register_blueprint(view, url_prefix='/')

	return app