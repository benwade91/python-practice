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


@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/1dfff59d067eedd4de16')
    blog_posts = response.json()
    return render_template('blog.html', posts=blog_posts)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    response = requests.get('https://api.npoint.io/1dfff59d067eedd4de16')
    blog_posts = response.json()
    post = next((blog for blog in blog_posts if blog['id'] == int(num)), None)
    print(post)
    return render_template('blog_post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)

