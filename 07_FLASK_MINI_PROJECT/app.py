# from flask import Flask, render_template, request, redirect, url_for
#
# from variables import DEBUG, PORT
# from db_utils import get_session, get_db_connection
# from utils import get_book, get_record_by_id
# from models import Book

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from variables import URI_DB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = URI_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
