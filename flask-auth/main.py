from flask import Flask, render_template, request, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        try:
            email = request.form.get('email')
            password = request.form.get('password')
            hashed_pw = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
            name = request.form.get('name')
            user = User(email=email, password=hashed_pw, name=name)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Logged in successfully.')
            if user.is_authenticated:
                return redirect('/secrets')
            else:
                return 'something went wrong!'
        except:
            flash('User already exists with that email! Try logging in!')
            return redirect('/login')
    else:
        return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user is None:
            error = 'Invalid credentials'
        else:
            if check_password_hash(pwhash=user.password, password=password):
                login_user(user)
                flash('Logged in successfully.')
                return redirect('/secrets')
            else:
                error = 'Invalid credentials'
    return render_template("login.html", error=error)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', 'files/cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
