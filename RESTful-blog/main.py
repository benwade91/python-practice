import datetime

from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route("/new-post", methods=['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('make-post.html', form=CreatePostForm())
    else:
        date = datetime.datetime.now().strftime("%B %d, %Y")
        title = request.form.get('title')
        subtitle = request.form.get('subtitle')
        author = request.form.get('author')
        img_url = request.form.get('img_url')
        body = request.form.get('body')
        post = BlogPost(date=date, title=title, subtitle=subtitle, author=author, img_url=img_url, body=body)
        db.session.add(post)
        db.session.commit()
        return redirect("/")


@app.route("/edit-post/<int:post_id>", methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    form = CreatePostForm(date=post.date, title=post.title, subtitle=post.subtitle, author=post.author,
                          img_url=post.img_url, body=post.body)
    if request.method == 'GET':
        return render_template('make-post.html', form=form)
    else:
        title = request.form.get('title')
        subtitle = request.form.get('subtitle')
        author = request.form.get('author')
        img_url = request.form.get('img_url')
        body = request.form.get('body')
        post.title = title
        post.subtitle = subtitle
        post.author = author
        post.img_url = img_url
        post.body = body
        db.session.commit()
        return redirect(f"/post/{post.id}")


@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/')

@app.route("/post/<int:index>")
def show_post(index):
    posts = db.session.query(BlogPost).all()
    requested_post = None
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
