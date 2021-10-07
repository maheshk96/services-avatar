from dataclasses import dataclass
from flask import Flask, jsonify, abort, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db/consultations'
CORS(app)

db = SQLAlchemy(app)

@dataclass
class User(db.Model):
    id: int
    first_name: str
    last_name: str
    email: str
    doctor: str
    consultation_location: str
    consultation_date: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    email = db.Column(db.String(200))
    doctor = db.Column(db.String(200), nullable=True)
    consultation_location = db.Column(db.String(200), nullable=True)
    consultation_date = db.Column(db.Date(), nullable=True)

@dataclass
class Location(db.Model):
    id: int
    location: str

    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200))

@app.route('/api/consults/<int:id>')
def index(id):
    req = requests.get('http://docker.for.mac.localhost:8000/api/consults/' + str(id))
    return jsonify(req.json())

@app.route('/api/consults/<int:id>', methods=['PUT'])
def bookConsultation(id):
    user = User.query.get(id)
    user.consultation_location = request.json.get('consultation_location')
    user.consultation_date = request.json.get('aconsultation_date')
    user.consultation_type = request.json.get('consultation_type')
    db.session.commit()
    return jsonify({
        'message': 'success'
    })

@app.route('/api/consults/<int:id>/confirm')
def getTestAppointment(id):
    user = User.query.get(id)
    return jsonify(user)

@app.route('/api/locations')
def getTestLocations():
    locations = Location.query.all()
    return jsonify(locations)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
