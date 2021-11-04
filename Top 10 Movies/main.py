from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movie-collection.db'
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
db = SQLAlchemy(app)


class EditForm(FlaskForm):
    rating = FloatField('Your rating out of 10', validators=[NumberRange(min=0, max=10, message="Chose a number between 0 and 10")])
    review = StringField('Your review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(240), unique=False, nullable=False)
    rating = db.Column(db.Float, unique=False, nullable=False)
    ranking = db.Column(db.Integer, unique=False, nullable=False)
    review = db.Column(db.String(240), unique=False, nullable=False)
    img_url = db.Column(db.String(240), unique=False, nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

db.create_all()


new_movie = Movie(
    title="Phone Booth",
    year=2002,
    description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
    rating=7.3,
    ranking=10,
    review="My favourite character was the caller.",
    img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
)
# db.session.add(new_movie)
# db.session.commit()


@app.route("/")
def home():
    all_movies = db.session.query(Movie).all()
    return render_template("index.html", movies=all_movies)

# @app.route("/add", methods=['GET', 'POST'])


@app.route("/delete/<movie_id>")
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect('/')

@app.route("/edit/<movie_id>", methods=['POST', 'GET'])
def edit(movie_id):
    movie = Movie.query.get(movie_id)
    form = EditForm()
    if request.method == 'GET':
        print(movie.title)
        return render_template('edit.html', movie=movie, form=form)
    elif form.validate_on_submit():
        rating = form.rating.data
        review = form.review.data
        movie.rating = rating
        movie.review = review
        db.session.commit()
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
