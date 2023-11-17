from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to simulate a database
books = [
    {"id": 1, "book_name": "Book1", "author": "Author1", "publisher": "Publisher1"},
    {"id": 2, "book_name": "Book2", "author": "Author2", "publisher": "Publisher2"}
]

# Get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({"books": books})

# Get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify({"book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        "id": len(books) + 1,
        "book_name": request.json['book_name'],
        "author": request.json['author'],
        "publisher": request.json['publisher']
    }
    books.append(new_book)
    return jsonify({"message": "Book created successfully", "book": new_book})

# Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book.update(request.json)
        return jsonify({"message": "Book updated successfully", "book": book})
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)
