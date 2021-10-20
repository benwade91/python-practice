from flask import Flask
import pages
import random

rand_number = random.randint(0, 9)

print(rand_number)

app = Flask(__name__)


@app.route('/')
def home():
    return pages.home


@app.route('/<int:number>')
def hello_world(number):
    if number > rand_number:
        return pages.too_high(number)
    elif number < rand_number:
        return pages.too_low(number)
    else:
        return pages.correct()


if __name__ == '__main__':
    app.run(debug=True)
