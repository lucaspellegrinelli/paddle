from app import app
from flask import render_template, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user
from app.usuario import Usuario
from app import db

def resposta_sucesso(conteudo):
    return jsonify({ "status": "sucesso", "conteudo": conteudo })

def resposta_erro(msg):
    return jsonify({ "status": "erro", "mensagem": msg })

@app.route("/api/login", methods=["POST"])
def login():
    nome_usuario = request.json.get("usuario")
    senha = request.json.get("senha")
    if nome_usuario is None or nome_usuario == "":
        return resposta_erro("Formulário inválido"), 400

    usuario = Usuario.query.filter_by(nome_usuario=nome_usuario).first()
    if usuario is None or not usuario.checar_senha(senha):
        return resposta_erro("Usuário ou senha inválido"), 401

    login_user(usuario, remember=False)
    return resposta_sucesso(None), 200

@app.route("/api/registrar", methods=["POST"])
def registrar():
    nome_usuario = request.json.get("usuario")
    senha = request.json.get("senha")
    if nome_usuario is None or senha is None:
        return resposta_erro("Formulário inválido"), 400
    if len(nome_usuario) < 3 or len(senha) < 8:
        return resposta_erro("Formulário inválido"), 400

    usuario = Usuario.query.filter_by(nome_usuario=nome_usuario).first()
    if usuario is not None:
        return resposta_erro("Nome de usuário indisponível"), 400

    usuario = Usuario(nome_usuario=nome_usuario)
    usuario.atualizar_senha(senha)
    db.session.add(usuario)
    db.session.commit()

    login_user(usuario, remember=False)
    return resposta_sucesso(None), 200

@app.route("/api/perfil")
@login_required
def dados_perfil():
    dados = {
        "id": current_user.id,
        "usuario": current_user.nome_usuario
    }
    return resposta_sucesso(dados), 200

@app.route("/api/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return resposta_sucesso(None), 200

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
    return resposta_sucesso(ultimos_3_posts), 200

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")
