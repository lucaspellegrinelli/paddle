from app import app
from flask import render_template, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user
from validate_email import validate_email
from app.usuario import Usuario
from app.usuario import Atleta
from app.post import Post
from app import db
import datetime
import functools

def resposta_sucesso(conteudo):
    return jsonify({ "status": "sucesso", "conteudo": conteudo })

def resposta_erro(msg):
    return jsonify({ "status": "erro", "mensagem": msg })

# Um decorador para proibir entrada de usuários comuns em rotas que requerem
# conta de administrador. Deve ser usado somente em conjunto com o decorador
#`login_required`
def requer_admin(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not current_user.admin:
            return resposta_erro("Acesso negado"), 403
        return func(*args, **kwargs)
    return wrapper

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

@app.route("/api/cadastro", methods=["POST"])
@login_required
@requer_admin
def cadastro():
    form = request.json
    nome_usuario = form.get("usuario")
    if nome_usuario is None or len(nome_usuario) < 3:
        return resposta_erro("Formulário inválido: nome de usuário inválido"), 400

    usuario = Usuario.query.filter_by(nome_usuario=nome_usuario).first()
    if usuario is not None:
        return resposta_erro("Nome de usuário indisponível"), 400

    email = form.get("email")
    if email is None or not validate_email(email):
        return resposta_erro("Formulário inválido: email inválido"), 400
    
    senha = form.get("senha")
    if senha is None or len(senha) < 8:
        return resposta_erro("Formulário inválido: senha inválida"), 400

    admin = form.get("admin")

    usuario = Usuario(nome_usuario=nome_usuario, email=email, admin=admin)
    usuario.atualizar_senha(senha)    
    db.session.add(usuario)
    db.session.commit()
    
    if form.get("dados_atleta"):
        id_usuario = usuario.id
        dados_atleta = form.get("dados_atleta")
        nome = dados_atleta.get("nome")

        nascimento_str = dados_atleta.get("nascimento")
        nascimento = datetime.datetime.strptime(nascimento_str, "%Y-%m-%d").date()
        federado = dados_atleta.get("federado")
        atleta = Atleta(id=id_usuario, nome=nome, nascimento=nascimento, federado=federado)
        db.session.add(atleta)
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

@app.route("/api/sessao")
def dados_sessao():
    logado = current_user is not None and current_user.is_authenticated
    admin = logado and current_user.admin
    return resposta_sucesso({
        "logado": logado,
        "admin": admin
    }), 200

@app.route("/api/informes")
def get_posts_recentes():
    limite = request.args.get('limite', default = None)
    if limite is None:
        posts = Post.query.order_by(Post.data.desc()).all()
    else:
        posts = Post.query.order_by(Post.data.desc()).limit(limite).all()
    return resposta_sucesso(posts), 200

@app.route("/api/informes/<id>")
def get_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        return resposta_erro("Post não encontrado"), 404
    return resposta_sucesso(post), 200

@app.route("/api/publicar", methods=["POST"])
def publicar_post():
    titulo = request.get_json().get('titulo')
    corpo = request.get_json().get('corpo')
    novo_post = Post(titulo=titulo, corpo=corpo)
    db.session.add(novo_post)
    db.session.commit()
    return resposta_sucesso(None), 200

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")
