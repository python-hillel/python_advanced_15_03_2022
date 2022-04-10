from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p><p>New line!</p>"

# http://google.com/test/value.html
# http://google.com/

# CRUD:     Create, Read, Update, Delete


@app.route("/")
def index():
    return render_template('index.html')
