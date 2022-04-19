from flask import Flask, render_template, request, redirect, url_for

from variables import DEBUG, PORT
from db_utils import get_session, get_db_connection
from utils import get_book, get_record_by_id
from models import Book


app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p><p>New line!</p>"

# http://google.com/test/value.html
# http://google.com/

# CRUD:     Create, Read, Update, Delete

s = get_session()


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
    books = s.query(Book).all()

    return render_template('books/list.html', books=books)


# @app.route('/books/detail/<int:book_id>')
# def detail_book(book_id):
#     connection = get_db_connection()
#     book = get_book(book_id, connection)
#     return render_template('books/detail.html', book=book)

@app.route('/books/detail/<int:book_id>')
def detail_book(book_id):
    book = get_record_by_id(book_id, s, Book)
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
            s.add(book)
            s.commit()
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
    book = get_record_by_id(book_id, s, Book)

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']

        book.title = title
        book.author = author

        if title and author:
            s.add(book)
            s.commit()

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
    book = get_record_by_id(book_id, s, Book)

    if request.method == 'POST':
        s.delete(book)
        s.commit()

        return redirect(url_for('list_books'))
    else:
        return render_template('books/delete.html', book=book)


if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)
