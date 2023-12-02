from website import create_app
from logger import logger

app = create_app()

if __name__ == '__main__':
	#logger.warning("application run")
	app.run(debug=True)
