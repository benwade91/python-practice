from flask import Flask, render_template
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home_route():
    year = datetime.now().year
    return render_template('index.html', year=year)

@app.route('/guess/<name>')
def guess(name):
    gender_api = requests.get(f"https://api.genderize.io?name={name}")
    gender = gender_api.json()['gender']
    age_api = requests.get(f"https://api.agify.io?name={name}")
    age = age_api.json()['age']
    return render_template('guess.html', name=name, gender=gender, age=age)

if __name__ == '__main__':
    app.run(debug=True)

