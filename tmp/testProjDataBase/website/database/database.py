from sqlalchemy import create_engine
from sqlalchemy.orm import Session

DB_NAME = "sqlite:///dataBase.db"

engine = create_engine(DB_NAME, echo=True)
session = Session(engine)