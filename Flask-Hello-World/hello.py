from flask import Flask

app = Flask(__name__)

print(__name__)


def bold(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def underline(func):
    def wrapper(*args, **kwargs):
        return f"<u>{func(*args, **kwargs)}</u>"
    return wrapper


def emphasis(func):
    def wrapper(*args, **kwargs):
        return f"<em>{func(*args, **kwargs)}</em>"
    return wrapper


@app.route('/')
def home():
    return 'hello'


@app.route('/<yo>')
@emphasis
def hello_world(yo):
    return f'{yo}'


if __name__ == '__main__':
    app.run(debug=True)
