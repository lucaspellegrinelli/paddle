from app import app
from flask import render_template, request
from flask_login import current_user, login_user
from app.user import User

@app.route("/api/test")
def test():
    return "ok"

@app.route("/api/login", methods=["POST"])
def login():
    # I'm using `request.json` instead of `request.form` because axios sends
    # POST requests serialized in json format for some reason
    username = request.json.get("username")
    pw = request.json.get("password")
    if username is None:
        return "invalid form"

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(pw):
        return "invalid username or password"

    login_user(user, remember=False)
    return "success"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")
