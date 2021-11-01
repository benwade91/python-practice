from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()
all_books = []


@app.route('/')
def home():
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('book_name', None)
        author = request.form.get('author', None)
        rating = request.form.get('rating', None)
        new_book = {
            'title': title,
            'author': author,
            'rating': rating
        }
        all_books.append(new_book)
        print(all_books)
        return redirect('/')
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

