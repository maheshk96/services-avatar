from dataclasses import dataclass
from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/appointment'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class User(db.Model):
    id: int
    first_name: str
    last_name: str
    email: str
    appointment_location: str
    appointment_date: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    appointment_location = db.Column(db.String(200), nullable=True)
    appointment_date = db.Column(db.Date(), nullable=True)

@dataclass
class Location(db.Model):
    id: int
    location: str

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200))

@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')