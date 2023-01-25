import sqlalchemy as sa
from sqlalchemy.dialects import mysql
import os
from app import db, app
from flask import url_for
from flask_login import UserMixin

class Cars(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    driver = db.Column(db.String(100), nullable=False)
    num_of_car = db.Column(db.String(100), nullable=False)
    on_line = db.Column(db.String(100), nullable=False)
    
    def __repr__(self):
        return '<Cars %r>' % self.name

class Order(db.Model, UserMixin):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    num_of_car = db.Column(db.String(100), nullable=False)
    driver = db.Column(db.String(100), nullable=False)
    client = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    num_of_phone = db.Column(db.String(100), nullable=False)
    sms_code = db.Column(db.String(100), nullable=False)
    time = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.name