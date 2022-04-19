from app import app, db
from flask import render_template, request, redirect, url_for

from sqlalchemy import or_

from webargs.flaskparser import use_kwargs
from webargs import fields

from models import Book
from utils import get_book
from variables import PORT, DEBUG

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p><p>New line!</p>"

# http://google.com/test/value.html
# http://google.com/

# CRUD:     Create, Read, Update, Delete

# s = get_session()


@app.route("/")
def index():
    return render_template('index.html')


# @app.route('/books/list')
# def list_books():
#     connection = get_db_connection()
#     books = connection.execute('SELECT * FROM books;').fetchall()
#     connection.close()
#     html = render_template('books/list.html', books=books)
#     print(html)
#     return html

@app.route('/books/list')
def list_books():
    # books = s.query(Book).all()
    books = Book.query.all()

    return render_template('books/list.html', books=books)


# @app.route('/books/detail/<int:book_id>')
# def detail_book(book_id):
#     connection = get_db_connection()
#     book = get_book(book_id, connection)
#     return render_template('books/detail.html', book=book)

@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    # book = get_record_by_id(book_id, s, Book)
    book = get_book(book_id)
    return render_template('books/detail.html', book=book)


# @app.route('/books/create', methods=['GET', 'POST'])
# def create_book():
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#
#         if title and author:
#             connection = get_db_connection()
#             connection.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
#             connection.commit()
#             connection.close()
#             return redirect(url_for('list_books'))
#
#     return render_template('books/create.html')


@app.route('/books/create', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            book = Book(title=title, author=author)
            db.session.add(book)
            db.session.commit()
            return redirect(url_for('list_books'))

    return render_template('books/create.html')


# @app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
# def update_book(book_id):
#     connection = get_db_connection()
#     book = get_book(book_id, connection)
#
#     if request.method == 'POST':
#         title = request.form['title']
#         author = request.form['author']
#
#         if title and author:
#             connection = get_db_connection()
#             connection.execute('UPDATE books SET title = ?, author = ? WHERE id = ?', (title, author, book_id))
#             connection.commit()
#             connection.close()
#             return redirect(url_for('list_books'))
#
#     return render_template('books/edit.html', book=book)

@app.route('/books/edit/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    # book = get_record_by_id(book_id, s, Book)
    book = get_book(book_id)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        if title and author:
            book.title = title
            book.author = author
            db.session.add(book)
            db.session.commit()

            return redirect(url_for('list_books'))

    return render_template('books/edit.html', book=book)


# @app.route('/books/delete/<int:book_id>', methods=('POST',))
# def delete_book(book_id):
#     if request.method == 'POST':
#         connection = get_db_connection()
#         connection.execute('DELETE FROM books WHERE id = ?', (book_id,))
#         connection.commit()
#         connection.close()
#
#         return redirect(url_for('list_books'))

@app.route('/books/delete/<int:book_id>', methods=['POST', 'GET'])
def delete_book(book_id):
    # book = get_record_by_id(book_id, s, Book)
    book = get_book(book_id)

    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()

        return redirect(url_for('list_books'))
    else:
        return render_template('books/delete.html', book=book)


@app.route('/books/search')
@use_kwargs(
    {
        'value': fields.Str(required=True)
    },
    location='query'
)
def search_book(value):
    """
        SELECT *
        FROM books
        WHERE title = '' OR author = '';
    """
    books = Book.query.filter(or_(Book.title == value, Book.author == value)).all()

    return render_template('books/search_res.html', books=books)


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
