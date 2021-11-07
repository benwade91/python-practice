from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random


app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def random_cafe():
    cafe_list = db.session.query(Cafe).all()
    cafe = random.choice(cafe_list)
    return jsonify(cafe=cafe.to_dict())


@app.route("/all")
def all_cafes():
    cafe_list = db.session.query(Cafe).all()
    return jsonify(cafes=[cafe.to_dict() for cafe in cafe_list])


@app.route("/search")
def city_search():
    city = request.args.get('location')
    cafe = Cafe.query.filter_by(location=city).first()
    if cafe is None:
        return '{"error": {"Not found": "Sorry, we don\'t have a cafe at that location"}}'
    else:
        return jsonify(cafe=cafe.to_dict())


@app.route("/add", methods=['POST'])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})


@app.route("/update-price/<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    if cafe is None:
        return '{"error": {"Not found": "Sorry, we don\'t have a cafe at that location"}}'
    else:
        cafe.coffee_price = request.form.get('new_price')
        db.session.commit()
        return jsonify(cafe=cafe.to_dict())


@app.route("/delete/<cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe = Cafe.query.get(cafe_id)
    user_api = request.args.get('api-key')
    if user_api == 'secretAPIKey':
        if cafe is None:
            return '{"error": {"Not found": "Sorry, we don\'t have a cafe at that location"}}'
        else:
            db.session.delete(cafe)
            db.session.commit()
            return '{"Success": "Cafe Closed"}'
    else:
        return '{"error": {"Wrong Credentials": "Sorry, you need the correct API Key"}}'
## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

