#!/usr/bin/python3
"""
Flask API with Basic Authentication and JWT Authentication
Implements role-based access control
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()

# 🔑 Secret key pour JWT - utiliser une variable d'environnement en production
app.config["JWT_SECRET_KEY"] =  'your_secret_key_here'

jwt = JWTManager(app)

# Users in memory
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# ----- Basic Auth -----
@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected route using Basic Authentication"""
    return "Basic Auth: Access Granted"


# ----- JWT Login -----
@app.route("/login", methods=["POST"])
def login():
    """Login endpoint that returns JWT token upon successful authentication"""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Create JWT token with user identity and role
        access_token = create_access_token(
            identity={'username': username,
                      'role': user['role']})
        return jsonify(access_token=access_token)
    return jsonify({"error": "Invalid credentials"}), 401


# ----- JWT Protected Route -----
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route using JWT Authentication"""
    return "JWT Auth: Access Granted"


# ----- Admin Only Route -----
@app.route("/admin-only" , methods=["GET"])
@jwt_required()
def admin_only():
    """Endpoint restricted to users with admin role"""
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# ----- JWT Error Handlers -----
@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401


# ----- Route d'accueil -----
@app.route("/")
def home():
    return jsonify({
        "message": "Flask API with Auth",
        "endpoints": {
            "POST /login": "Get JWT token",
            "GET /basic-protected": "Basic Auth protected",
            "GET /jwt-protected": "JWT protected",
            "GET /admin-only": "Admin only (JWT)"
        }
    })


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)