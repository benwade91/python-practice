from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
        return redirect('/')
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)

