from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from logger import logger

IS_CREATED = True

DB_NAME = "sqlite:///dataBase.db"
logger.warning(f"create database NAME: {DB_NAME}")

engine = create_engine(DB_NAME, echo=True)
logger.warning("create engine")
session = Session(engine)
logger.warning("create session")

def notCreated():
	pass