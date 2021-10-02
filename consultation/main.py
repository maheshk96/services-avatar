from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from dataclasses import dataclass
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/consultation'
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
class Consultation(db.Model):
    id: int
    doctor = str
    appointment = str
    type = str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    doctor = db.Column(db.String(200))
    appointment = db.Column(db.Date(), nullable=True)
    type = db.Column(db.String(200))

@dataclass
class Location(db.Model):
    id: int
    location: str

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200))

@app.route('/')
def index():
    return 'Hello'

@app.route('/api/consults/<int:id>', methods=['PUT'])
def bookConsult(id):
    consults = Consultation.query.get(id)
    consults.doctor = request.json.get('doctor')
    consults.type = request.json.get('type')
    db.session.commit()
    return jsonify({
        'message': 'success'
    })

@app.route('/api/consults/<int:id>/confirm')
def getConsultConfirm(id):
    consults = Consultation.query.get(id)
    return jsonify(consults)

@app.route('/api/doctors')
def getDoctorInfo():
    consultations = Consultation.query.all()
    return jsonify(consultations)

@app.route('/api/locations')
def getTestLocations():
    locations = Location.query.all()
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')