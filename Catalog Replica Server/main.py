from FlaskSetup import app
from flask_cors import CORS
from APIs.search import query_books_by_subject
from APIs.info import query_book_by_item
from APIs.purchase import purchase_item
from APIs.consistent_book_count import consistent_book_count
from APIs.updateBook import updateBooks
from APIs.add_book import addBook
CORS(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
