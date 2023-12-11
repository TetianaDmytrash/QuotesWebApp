import os
from .logger import logger

def create_app():

	from flask import Flask
	logger.warning(f"create flask")
	app = Flask(__name__)

	from .database.database import engine, DB_NAME

	if os.path.exists(DB_NAME):
		logger.warning("Database exists.")
	else:
		logger.warning("Database does not exist.")

		from .database.models import Base
		logger.warning(f"clear database")
		# Очистка базы данных
		Base.metadata.drop_all(engine)

		logger.warning(f"create tables in database")
		# Создание таблиц в базе данных
		Base.metadata.create_all(engine)

		from .database.fillDatabase import fillDatabase
		logger.warning(f"fill database")
		# Наполнение базы данных
		fillDatabase()

	from .route import route
	app.register_blueprint(route, url_prefix='/')


	return app