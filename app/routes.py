from app import app
from flask import render_template, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user
from app.user import User
from app import db

@app.route("/api/test")
def test():
    return "ok"

@app.route("/api/login", methods=["POST"])
def login():
    # I'm using `request.json` instead of `request.form` because axios sends
    # POST requests serialized in json format for some reason
    username = request.json.get("username")
    pw = request.json.get("password")
    if username is None or username == "":
        return "invalid form", 400

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(pw):
        return "invalid username or password", 401

    login_user(user, remember=False)
    return "success", 200

@app.route("/api/register", methods=["POST"])
def register():
    # I'm using `request.json` instead of `request.form` because axios sends
    # POST requests serialized in json format for some reason
    username = request.json.get("username")
    pw = request.json.get("password")
    if username is None or pw is None:
        return "invalid form", 400
    if len(username) < 3 or len(pw) < 8:
        return "invalid form", 400

    user = User.query.filter_by(username=username).first()
    if user is not None:
        return "username not available", 400

    user = User(username=username)
    user.set_password(pw)
    db.session.add(user)
    db.session.commit()

    login_user(user, remember=False)
    return "success", 200

@app.route("/api/profile")
@login_required
def get_profile_data():
    return jsonify({
        "id": current_user.id,
        "username": current_user.username
    })

@app.route("/api/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return "success"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")
