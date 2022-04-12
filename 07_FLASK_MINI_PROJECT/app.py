import sqlite3

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.exceptions import abort

from variables import DEBUG, PORT, URL

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p><p>New line!</p>"

# http://google.com/test/value.html
# http://google.com/

# CRUD:     Create, Read, Update, Delete

def get_db_connection():
    connection = sqlite3.connect(URL)
    connection.row_factory = sqlite3.Row
    return connection


def get_book(book_id):
    connection = get_db_connection()
    book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
    connection.close()
    if book is None:
        abort(404)
    else:
        return book


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/books/list')
def list_books():
    connection = get_db_connection()
    books = connection.execute('SELECT * FROM books;').fetchall()
    connection.close()
    return render_template('books/list.html', books=books)


@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    book = get_book(book_id)
    return render_template('books/detail.html', book=book)


@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            connection = get_db_connection()
            connection.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
            connection.commit()
            connection.close()
            return redirect(url_for('list_books'))

    return render_template('books/create.html')


@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    book = get_book(book_id)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            connection = get_db_connection()
            connection.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, book_id))
            connection.commit()
            connection.close()
            return redirect(url_for('list_books'))

    return render_template('books/edit.html', book=book)


@app.route('/books/delete/<int:book_id>', methods=('POST',))
def delete_book(book_id):
    if request.method == 'POST':
        connection = get_db_connection()
        connection.execute('DELETE FROM books WHERE id = ?', (book_id,))
        connection.commit()
        connection.close()

        return redirect(url_for('list_books'))


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
