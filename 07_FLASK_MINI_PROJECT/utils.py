from models import Book
from werkzeug.exceptions import abort

# def get_book(book_id, connection):
#     book = connection.execute('SELECT * FROM books WHERE id = ?', (book_id,)).fetchone()
#     connection.close()
#     if book is None:
#         abort(404)
#     else:
#         return book


def get_book(book_id):
    book = Book.query.filter_by(id=book_id).one()
    if book is None:
        abort(404)
    else:
        return book


def get_record_by_id(record_id, session, model):
    record = session.query(model).filter_by(id=record_id).one()
    if record is None:
        abort(404)
    else:
        return record
