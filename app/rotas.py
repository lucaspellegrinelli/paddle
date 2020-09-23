from app import app
from sqlalchemy import func
from flask import render_template, request, jsonify
from flask_login import current_user, login_user, login_required, logout_user
from validate_email import validate_email
from app.usuario import Usuario, Atleta, Categoria
from app.campeonato import Campeonato, Participantes, Estilo, Partidas
from app.post import Post
from app import db
import json
import datetime
import functools
import sqlalchemy
from sqlalchemy.sql import text

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

    admin = form.get("admin") == True

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
        sexo = dados_atleta.get("sexo")
        categoria = dados_atleta.get("categoria")
        print(categoria)

        atleta = Atleta(id=id_usuario, nome=nome, nascimento=nascimento, federado=federado,
                        sexo=sexo, categoria=categoria, pontuacao=0)
        db.session.add(atleta)
        db.session.commit()

    login_user(usuario, remember=False)
    return resposta_sucesso(None), 200

@app.route("/api/perfil")
@login_required
def dados_perfil():
    dados = {
        "id": current_user.id,
        "usuario": current_user.nome_usuario,
        "email": current_user.email
    }

    atleta = Atleta.query.filter_by(id=current_user.id).first()
    if atleta is not None:
        categoria = Categoria.query.filter_by(id=atleta.categoria).first()
        dados["dados_atleta"] = {
            "nome": atleta.nome,
            "nascimento": atleta.nascimento.strftime("%d/%m/%Y"),
            "federado": atleta.federado,
            "pontuacao": atleta.pontuacao,
            "sexo": atleta.sexo,
            "categoria": categoria.nome,
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

@app.route("/api/informes", methods=["GET"])
def get_posts_recentes():
    limite = request.args.get('limite', default = None)
    if limite is None:
        posts = Post.query.order_by(Post.data.desc()).all()
    else:
        posts = Post.query.order_by(Post.data.desc()).limit(limite).all()
    return resposta_sucesso(posts), 200

@app.route("/api/informes", methods=["POST"])
@login_required
@requer_admin
def publicar_post():
    titulo = request.get_json().get('titulo')
    corpo = request.get_json().get('corpo')
    novo_post = Post(titulo=titulo, corpo=corpo)
    db.session.add(novo_post)
    db.session.commit()
    return resposta_sucesso(None), 200

@app.route("/api/informes/<id>", methods=["GET"])
def get_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        return resposta_erro("Post não encontrado"), 404
    return resposta_sucesso(post), 200

@app.route("/api/informes/<id>", methods=["DELETE"])
@login_required
@requer_admin
def deletar_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        return resposta_erro("Post não encontrado"), 404    
    db.session.delete(post)
    db.session.commit()
    return resposta_sucesso(None), 200    

@app.route("/api/informes/<id>", methods=["PATCH"])
@login_required
@requer_admin
def editar_post(id):
    post = Post.query.filter_by(id=id).first()
    if not post:
        return resposta_erro("Post não encontrado"), 404
    titulo = request.get_json().get('titulo')
    corpo = request.get_json().get('corpo')    
    post.titulo = titulo
    post.corpo = corpo
    db.session.commit()
    return resposta_sucesso(None), 200 

@app.route("/api/categorias", methods=["GET"])
def get_categorias():
    categorias = Categoria.query.all()
    resultado = []
    for c in categorias:
        resultado.append({ "text": c.nome, "value": c.id })
    return resposta_sucesso(resultado), 200

@app.route("/api/atletas", methods=["GET"])
def get_atletas():
    atletas = []
    filtros = dict()

    for filtro in request.args:
        chave = text(filtro)
        valor = request.args.get(filtro)
        if(valor is not None and valor != "" and filtro != "nome"):
            filtros[chave] = valor

    nome = request.args.get("nome")
    if (nome is not None and nome != ""):
        atletas = Atleta.query.filter(Atleta.nome.like(f"%{nome}%")).filter(*filtros).all()
    else:    
        atletas = Atleta.query.filter(*filtros).all()
    categorias = Categoria.query.filter().all()
    categorias = {row.id : row.nome for row in categorias}
    for atleta in atletas:
        atleta.categoria = categorias[atleta.categoria]
    return resposta_sucesso(atletas), 200
    
@app.route("/api/campeonatos", methods=["GET"])
def get_campeonatos():
    result = db.session.query(
        Campeonato.id,
        Campeonato.nome,
        Campeonato.data,
        Campeonato.capacidade,
        Campeonato.estilo,
        Campeonato.comentarios,
        func.count(Participantes.id)
    ).join(
        Participantes,
        (Participantes.id_camp == Campeonato.id) & (Participantes.aprovado == 1),
        isouter=True
    ).group_by(Campeonato.id).all()

    def line_to_dict(l):
        d = datetime.datetime.strptime(str(l[2]), '%Y-%m-%d')
        s = (d - datetime.datetime(1970,1,1)).total_seconds()

        return {
            "id": l[0],
            "nome": l[1],
            "data": s,
            "capacidade": l[3],
            "estilo": l[4],
            "comentarios": l[5],
            "participantes": l[6]
        }

    result = [line_to_dict(l) for l in result]
    return resposta_sucesso(result), 200

@app.route("/api/atualizar_campeonato", methods=["POST"])
@login_required
@requer_admin
def atualizar_campeonatos():
    id_camp = request.get_json().get('id')
    camp = db.session.query(Campeonato).filter(Campeonato.id == id_camp).first()
    camp.nome = request.get_json().get('nome')
    camp.data = datetime.datetime.fromtimestamp(request.get_json().get('data') / 1000.0)
    camp.capacidade = request.get_json().get('capacidade')
    camp.estilo = request.get_json().get('estilo')
    camp.comentarios = request.get_json().get('comentarios')
    db.session.commit()
    return resposta_sucesso(None), 200

@app.route("/api/participantes", methods=["POST"])
def get_participantes():
    id_camp = request.get_json().get('id_camp')

    result = db.session.query(
        Participantes.id_atleta,
        Atleta.nome,
        Participantes.aprovado
    ).join(
        Atleta,
        Participantes.id_atleta == Atleta.id
    ).filter(
        Participantes.id_camp == id_camp
    ).all()

    def line_to_dict(l):
        return {
            "id_atleta": l[0],
            "nome_atleta": l[1],
            "aprovado": l[2]
        }

    result = [line_to_dict(l) for l in result]
    return resposta_sucesso(result), 200

@app.route("/api/aprovar_participantes", methods=["POST"])
def aprovar_participantes():
    ids = request.get_json().get('ids')

    for i in ids:
        part = db.session.query(Participantes).filter(Participantes.id_atleta == i).first()
        part.aprovado = 1
        db.session.commit()

    return resposta_sucesso(None), 200

@app.route("/api/inscricao", methods=["POST"])
@login_required
def inscricao_campeonato():
    id_camp = request.get_json().get('id_camp')
    id_atleta = request.get_json().get('id_atleta')
    print("Inscricao", id_camp, id_atleta)
    if id_atleta == current_user.id or current_user.admin:
        novo_participantes = Participantes(id_camp=id_camp, id_atleta=id_atleta, aprovado=0)
        db.session.add(novo_participantes)
        db.session.commit()
        return resposta_sucesso(None), 200
    else:
        return resposta_erro("Id de usuário inválido"), 400

@app.route("/api/desinscricao", methods=["POST"])
@login_required
def desinscricao_campeonato():
    id_camp = request.get_json().get('id_camp')
    id_atleta = request.get_json().get('id_atleta')
    print("Desinscricao", id_camp, id_atleta)
    if id_atleta == current_user.id or current_user.admin:
        target = db.session.query(
            Participantes
        ).filter(
            Participantes.id_atleta == id_atleta
        ).filter(
            Participantes.id_camp == id_camp
        ).first()

        db.session.delete(target)
        db.session.commit()
        return resposta_sucesso(None), 200
    else:
        return resposta_erro("Id de usuário inválido"), 400

@app.route("/api/inscricoes", methods=["POST"])
@login_required
def get_inscricoes():
    id_atleta = request.get_json().get('id_atleta')
    if id_atleta == current_user.id or current_user.admin:

        result = db.session.query(
            Campeonato.id,
            Participantes.aprovado
        ).join(
            Participantes,
            Participantes.id_atleta == id_atleta
        ).all()

        def line_to_dict(l):
            return {
                "id": l[0],
                "aprovado": l[1]
            }

        result = [line_to_dict(l) for l in result]
        return resposta_sucesso(result), 200
    else:
        return resposta_erro("Id de usuário inválido"), 400

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html")

@app.route("/api/estilos", methods=["GET"])
def get_estilos():

    result = db.session.query(
        Estilo.id,
        Estilo.nome.label("estilo"),
    ).all()

    def return_estilo(l):
        return {
            "id": l[0],
            "estilo": l[1]
        }

    result = [return_estilo(l) for l in result]
    return resposta_sucesso(result), 200


@app.route("/api/criar_camp", methods=["POST"])
@login_required
@requer_admin
def criar_camp():

    form = request.json
    print (form)
    nome = form.get("nome")
    data = datetime.datetime.fromtimestamp(form.get("data") / 1000.0)
    capacidade = form.get("capacidade")
    estilo = form.get("estilo")
    comentarios = form.get("comentarios")

    campeonato = Campeonato(nome=nome, data=data, capacidade=capacidade, estilo=estilo, comentarios=comentarios)   
    db.session.add(campeonato)
    db.session.commit()
    return resposta_sucesso(None), 200

@app.route("/api/classificacao_camp/<id>", methods=["GET"])

def get_classificacao(id):
    id_camp = str(id)
  
    sql_query = sqlalchemy.text("SELECT atleta.nome, COUNT(partida.id) AS vitorias\
                                FROM participantes\
                                LEFT JOIN partida ON\
                                ((partida.id_atleta1 = participantes.id_atleta AND partida.resultado = 1)\
                                OR (partida.id_atleta2 = participantes.id_atleta AND partida.resultado = -1))\
                                AND partida.id_camp = participantes.id_camp\
                                INNER JOIN atleta ON participantes.id_atleta = atleta.id\
                                WHERE participantes.id_camp =" + id_camp + "\
                                GROUP BY participantes.id_atleta")

    result = db.session.execute(sql_query)
    result_as_list = result.fetchall()
    result_as_list = [dict(row) for row in result_as_list]
    
    print(result_as_list)
    return resposta_sucesso(result_as_list), 200
