from flask import Flask
from domain.model.db import db


def initialize_db(app: Flask):
    with app.app_context():
        db.init_app(app)
        db.create_all()