import os
from flask import Flask, render_template, abort, send_from_directory, render_template, request
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
application = app

app.config.from_pyfile('config.py')


convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

metadata = MetaData(naming_convention=convention)
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

from auth import bp as auth_bp, init_login_manager

app.register_blueprint(auth_bp)


init_login_manager(app)

from models import Order, Cars

@app.route('/')
def index():
    cars = Cars.query.filter_by(on_line='no').all()
    sms_codes = Order.query.all()
    return render_template('index.html', cars=cars, sms_codes=sms_codes)

@app.route('/<string:sms_code>/info')
def info(sms_code):
    order = Order.query.filter_by(sms_code=sms_code).first()
    return render_template('info.html', order=order)