from flask import Blueprint, make_response, jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/home', methods=['GET'])
def home():
    return make_response(jsonify({'msg': 'home'}))

