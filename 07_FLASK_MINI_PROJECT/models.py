from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from datetime import datetime

from variables import URI_DB

base = declarative_base()


class Book(base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    author = Column(String(100), nullable=False)
    created = Column(DateTime, default=datetime.now)
    updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __str__(self):
        return f'{self.author} - {self.title}'


engin = create_engine(URI_DB)
base.metadata.create_all(engin)
