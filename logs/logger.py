"""
logging set up
"""
import logging


class NoSQLFilter(logging.Filter):
    """
    filter for string that I won`t to process
    """
    def filter(self, record):
        """
        filter
        :param record:
        :return:
        """
        # Return False for records you want to exclude from processing
        return not record.getMessage().startswith("sqlalchemy.engine.Engine")


# Logger setup
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Example of a log entry using a specific format
logger.info("This is an info message.")


# Setting up a handler for writing to a file
file_handler = logging.FileHandler("logfile.log")
file_handler.setLevel(logging.WARNING)

# Determining the format of log entries
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Adding a handler to the logger
logger.addHandler(file_handler)

# logger.warning("WARNING")
# logger.error("ERROR")
# logger.critical("CRITICAL")
