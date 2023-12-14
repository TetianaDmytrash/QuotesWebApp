"""
file with constant
is set to true if the database is created, and you do not want to overwrite it
is set to false if you want to delete the existing database and create a new one
"""
import os

DATABASE_FILE_PATH = "sqlite:///app/database/data_base.db"
IS_CREATED = os.path.exists(os.getcwd() + "/app/database/data_base.db")
