import sqlite3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from models import base
from variables import DB_NAME, URI_DB


def get_db_connection():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    return connection


def get_session():
    engin = create_engine(URI_DB)
    base.metadata.bind = engin
    db_session = sessionmaker(bind=engin)
    return db_session()
