from app import app, db
from datetime import date
from dataclasses import dataclass

@dataclass
class Post(db.Model):
    id: int
    titulo: str
    corpo: str 
    data: date

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data = db.Column(db.Date, nullable=False, default=date.today())

    def __repr__(self):
        return f"Post({self.titulo})"