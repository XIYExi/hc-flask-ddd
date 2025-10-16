from flask import Blueprint, make_response, jsonify
from application.user_service import verify

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['GET'])
def login():
    result = verify()
    return make_response(jsonify({'username': 'xiye', 'password': '123456', 'result': result}))


@user_bp.route('/logout', methods=['GET'])
def logout():
    return make_response(jsonify({'msg': 'success logout'}))

@user_bp.route('/register', methods=['GET'])
def register():
    return make_response(jsonify({'msg': 'register success!'}))

