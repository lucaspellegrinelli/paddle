from flask import Flask

app = Flask(__name__,
            static_folder = "../client/dist/assets",
            static_url_path = "/assets",
            template_folder = "../client/dist")

from app import routes
