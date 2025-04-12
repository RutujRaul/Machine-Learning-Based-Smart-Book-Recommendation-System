from flask import Blueprint, request, jsonify
from config import get_db
from models.user_model import create_user, get_user_by_email, verify_user_password
from utils.jwt_helper import generate_token

auth_bp = Blueprint("auth", __name__)

db = get_db()

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not all([username, email, password]):
        return jsonify({"error": "All fields are required"}), 400

    user_id = create_user(db, username, email, password)
    if user_id is None:
        return jsonify({"error": "User already exists"}), 409

    token = generate_token(user_id)
    return jsonify({"message": "User created", "token": token}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not all([email, password]):
        return jsonify({"error": "Email and password are required"}), 400

    user = get_user_by_email(db, email)
    if not user or not verify_user_password(user, password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = generate_token(user["_id"])
    return jsonify({"message": "Login successful", "token": token}), 200
