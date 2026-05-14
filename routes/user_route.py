from flask import Blueprint, request, jsonify # type: ignore
from services.user_service import create_user, get_all_users

user_bp = Blueprint("users", __name__)

@user_bp.route("/", methods=["GET"])
def get_users():
    return jsonify(get_all_users())

@user_bp.route("/", methods=["POST"])
def add_user():
    data = request.get_json()
    user = create_user(data)
    return jsonify(user), 201