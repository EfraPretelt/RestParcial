from app import db


class Checks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numofcheck = db.Column(db.String(50))
    destination = db.Column(db.String(50))
    name = db.Column(db.String(60))
    identification = db.Column(db.Integer, nullable=False)
    paquete = db.Column(db.String(15))
    price = db.Column(db.Integer)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    postalCode = db.Column(db.Integer, nullable=False)
    identification = db.Column(db.Integer, nullable=False)
