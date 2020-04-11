from app import app, db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Post(db.Model):
    id: int
    titulo: str
    corpo: str 
    data: datetime

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    corpo = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post({self.titulo})"