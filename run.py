"""
file starts whole app
"""
from app import create_app
from logs.logger import logger

app = create_app()

if __name__ == '__main__':
	logger.warning("application run")
	# app.run(debug=True)
	app.run(host="0.0.0.0", port=8080)
