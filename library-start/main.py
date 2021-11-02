from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()


@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    return render_template('index.html', library=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form.get('book_name', None)
        author = request.form.get('author', None)
        rating = float(request.form.get('rating', None))

        harry_p = Book(title=title, author=author, rating=rating)
        db.session.add(harry_p)
        db.session.commit()

        return redirect('/')
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=False)

