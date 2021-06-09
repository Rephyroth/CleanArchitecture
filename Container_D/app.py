from flask import Flask,request, render_template, jsonify, abort
from models import Book
from peewee import DoesNotExist

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/my-books', methods=['GET', 'POST'])
def books():
    return jsonify([{"id_book": book.id_book, "title": book.title, "isbn": book.isbn, "author": book.author, "publisher": book.publisher, "genre": book.genre, "num_pages": book.num_pages, "year": book.year} for book in Book.select()])

@app.route('/my-books/<book_id>')
def book(book_id):
    try:
        book = Book.get(Book.id_book == book_id)
        return render_template('book.html', id=book.id_book, title=book.title, author=book.author, year=book.year)
    except DoesNotExist:
        abort(404)
    except:
        abort(500)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)