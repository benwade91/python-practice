from flask import Flask, render_template, request
import requests
import smtplib
import os

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/1dfff59d067eedd4de16')
    blog_posts = response.json()
    return render_template('index.html', posts=blog_posts)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact(title='Contact'):
    return render_template('contact.html', title=title)

@app.route('/post/<post_id>')
def post(post_id):
    response = requests.get('https://api.npoint.io/1dfff59d067eedd4de16')
    posts = response.json()
    post = next((article for article in posts if article['id'] == int(post_id)), None)
    return render_template('post.html', post=post)

@app.route('/email', methods=['GET','POST'])
def email():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        print(name)
        print(email)
        print(phone)
        print(message)
        with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:
            connection.starttls()
            connection.login(user=os.environ.get('FROM_EMAIL'), password=os.environ.get('YAHOO_PW'))
            connection.sendmail(
                from_addr=os.environ.get('FROM_EMAIL'),
                to_addrs=os.environ.get('TO_EMAIL'),
                msg=f"Subject:{name} {email}\n\n "
                    f"{message}")
        return contact(title='Success!')

if __name__ == '__main__':
    app.run(debug=True)