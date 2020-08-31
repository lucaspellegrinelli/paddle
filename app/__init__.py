from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from app.config import Config

app = Flask(__name__,
            static_folder = "../client/dist/assets",
            static_url_path = "/assets",
            template_folder = "../client/dist")

app.config.from_object(Config)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from app import usuario
from app import rotas
