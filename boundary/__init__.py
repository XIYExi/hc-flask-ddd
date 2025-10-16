from flask import Flask
from flasgger import Swagger
from boundary.main_route import main_bp
from boundary.user_route import user_bp



def initialize_route(app: Flask):
    with app.app_context():
        app.register_blueprint(main_bp, url_prefix='/api/v1/main')
        app.register_blueprint(user_bp, url_prefix='/api/v1/user')


def initialize_swagger(app: Flask):
    with app.app_context():
        swagger = Swagger(app)
        return swagger