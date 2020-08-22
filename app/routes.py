from app import app
from flask import render_template

@app.route("/api/test")
def test():
    return "ok"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")
