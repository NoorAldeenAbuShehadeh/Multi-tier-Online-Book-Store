from flask_cors import CORS
from FlaskSetup import app
from APIs.info import query_book_by_item
from APIs.search import query_books_by_subject
from APIs.purchase import purchase_item
from APIs.update_book import update_book
from APIs.add_book import add_book
CORS(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
