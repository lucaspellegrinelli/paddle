from app import app
from flask import render_template, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user
from app.user import User
from app import db

def response_success(data):
    return jsonify({ "status": "success", "data": data })

def response_error(msg):
    return jsonify({ "status": "error", "message": msg })

@app.route("/api/test")
def test():
    return make_response(True, None)

@app.route("/api/login", methods=["POST"])
def login():
    # I'm using `request.json` instead of `request.form` because axios sends
    # POST requests serialized in json format for some reason
    username = request.json.get("username")
    pw = request.json.get("password")
    if username is None or username == "":
        return response_error("Invalid form"), 400

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(pw):
        return response_error("Invalid username or password"), 401

    login_user(user, remember=False)
    return response_success(None), 200

@app.route("/api/register", methods=["POST"])
def register():
    # I'm using `request.json` instead of `request.form` because axios sends
    # POST requests serialized in json format for some reason
    username = request.json.get("username")
    pw = request.json.get("password")
    if username is None or pw is None:
        return response_error("Invalid form"), 400
    if len(username) < 3 or len(pw) < 8:
        return response_error("Invalid form"), 400

    user = User.query.filter_by(username=username).first()
    if user is not None:
        return response_error("Username not available"), 400

    user = User(username=username)
    user.set_password(pw)
    db.session.add(user)
    db.session.commit()

    login_user(user, remember=False)
    return response_success(None), 200

@app.route("/api/profile")
@login_required
def get_profile_data():
    data = {
        "id": current_user.id,
        "username": current_user.username
    }
    return response_success(data), 200

@app.route("/api/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return response_success(None), 200

@app.route("/api/home")
def get_recent_posts():
    ultimos_3_posts = [
        { 
          id: 1,
          titulo: 'Postagem nº1',
          data: '07/04/2020',
          corpo: 'Um teste'
        },
        { 
          id: 2,
          titulo: 'Postagem nº2',
          data: '08/04/2020',
          corpo: 'Outro teste'
        },
        { 
          id: 3,
          titulo: 'Postagem nº3',
          data: '08/04/2020',
          corpo: 'Outro teste'
        }
    ]
    return response_success(ultimos_3_posts), 200

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")
