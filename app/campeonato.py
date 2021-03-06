from app import app, db, login_manager
import bcrypt
from flask_login import UserMixin
from dataclasses import dataclass
from datetime import date

@dataclass
class Campeonato(db.Model):
	id: int
	nome: str
	data: date
	capacidade: int
	estilo: int
	comentarios: str

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String(128))
	data = db.Column(db.Date)
	capacidade = db.Column(db.Integer)
	estilo = db.Column(db.Integer)
	comentarios = db.Column(db.String(512))

	def __repr__(self):
		return f"Campeonato({self.nome})"

@dataclass
class Estilo(db.Model):
	id: int
	nome: str

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.Text)

@dataclass
class Participantes(db.Model):
	id: int
	id_camp: int
	id_atleta: int
	aprovado: int

	id = db.Column(db.Integer, primary_key=True)
	id_camp = db.Column(db.Integer)
	id_atleta = db.Column(db.Integer)
	aprovado = db.Column(db.Integer)

@dataclass
class Partidas(db.Model):
	id: int
	id_atleta1: int
	id_atleta2: int
	id_camp: int
	resultado: int

	id = db.Column(db.Integer, primary_key=True)
	id_atleta1 = db.Column(db.Integer)
	id_atleta2 = db.Column(db.Integer)
	id_camp = db.Column(db.Integer)
	resultado = db.Column(db.Integer)