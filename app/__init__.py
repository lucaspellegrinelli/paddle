from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

app = Flask(__name__,
            static_folder = "../client/dist/assets",
            static_url_path = "/assets",
            template_folder = "../client/dist")

app.config.from_object(Config)
db = SQLAlchemy(app)

from app.models import User

db.create_all()
db.session.commit()

from app import routes
