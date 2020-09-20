from app import app, db, login_manager
import bcrypt
from flask_login import UserMixin
from dataclasses import dataclass
from datetime import date

class Usuario(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(64), index=True, unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    senha_hash = db.Column(db.String(128))
    admin = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"Usuario({self.nome_usuario})"

    def atualizar_senha(self, senha):
        senha = senha.encode()
        if len(senha) > 72:
            app.logger.warning(
                "`bcrypt` tem um limite de 72 caracteres, qualquer coisa além disso será ignorada"
            )
        self.senha_hash = bcrypt.hashpw(senha, bcrypt.gensalt())

    def checar_senha(self, senha):
        return bcrypt.checkpw(senha.encode(), self.senha_hash)

@dataclass
class Atleta(db.Model):
    id: int
    nome: str
    nascimento: date
    federado: bool
    pontuacao: int


    id = db.Column(db.Integer, db.ForeignKey('usuario.id'), primary_key=True)
    nome = db.Column(db.String(64))
    nascimento = db.Column(db.Date)
    federado = db.Column(db.Boolean)
    pontuacao = db.Column(db.Integer)

@login_manager.user_loader
def carregar_usuario(id):
    return Usuario.query.get(int(id))
