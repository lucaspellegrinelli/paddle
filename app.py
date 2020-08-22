from flask import Flask, render_template

app = Flask(__name__,
            static_folder = "./client/dist/assets",
            static_url_path = "/assets",
            template_folder = "./client/dist")

@app.route("/api/test")
def test():
    return "ok"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    print(path)
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
