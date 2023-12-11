"""
file with database connect
start session
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from logs.logger import logger

DB_NAME = "sqlite:///dataBase.db"
logger.warning("connect database NAME: {}".format(DB_NAME))

engine = create_engine(DB_NAME, echo=True)
logger.warning("create engine")
session = Session(engine)
logger.warning("create session")
