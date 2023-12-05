from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from project.logger import logger

DB_NAME = "sqlite:///dataBase.db"
logger.warning(f"connect database NAME: {DB_NAME}")

engine = create_engine(DB_NAME, echo=True)
logger.warning("create engine")
session = Session(engine)
logger.warning("create session")

