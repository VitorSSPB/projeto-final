from functools import wraps

from flask import Flask, render_template, request, redirect, url_for, flash, session, g
import mysql.connector

import repositorio
from models import Chamado, Equipamento, Usuario

app = Flask(__name__)
app.secret_key = "controle-equipamentos-etec"


@app.before_request
def carregar_usuario():
    g.usuario = None
    if "usuario_id" in session:
        g.usuario = repositorio.buscar_usuario(session["usuario_id"])
        if g.usuario is None:
            session.clear()


def exige(acao):
    def decorador(funcao):
        @wraps(funcao)
        def verificar(*args, **kwargs):
            if g.usuario is None:
                flash("Entre com seu usuário para continuar.", "erro")
                return redirect(url_for("login", proxima=request.path))
            if not g.usuario.pode(acao):
                flash("Seu perfil não tem permissão para esta ação.", "erro")
                return redirect(url_for("inoperantes"))
            return funcao(*args, **kwargs)
        return verificar
    return decorador


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = repositorio.buscar_usuario_por_login(request.form["login"])
        if usuario is None or not usuario.verificar_senha(request.form["senha"]):
            flash("Login ou senha incorretos.", "erro")
            return render_template("login.html")
        session.clear()
        session["usuario_id"] = usuario.id
        flash(f"Bem-vindo, {usuario.nome}!")
        proxima = request.args.get("proxima", "")
        if not proxima.startswith("/") or proxima.startswith("//"):
            proxima = url_for("inoperantes")
        return redirect(proxima)

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("Você saiu do sistema.")
    return redirect(url_for("login"))


@app.route("/")
def inicio():
    """Abre a página inicial."""
    return redirect(url_for("inoperantes"))


@app.route("/abrir", methods=["GET", "POST"])
@exige("abrir_chamado")
def abrir_chamado():
    """Abre um novo chamado."""
    if request.method == "POST":
        try:
            chamado = Chamado(request.form["equipamento_id"], request.form["descricao_problema"])
            repositorio.salvar_chamado(chamado)
            flash("Chamado aberto com sucesso!")
            return redirect(url_for("inoperantes"))
        except ValueError as erro:
            flash(str(erro), "erro")

    equipamentos = repositorio.listar_equipamentos()
    return render_template("abrir_chamado.html", equipamentos=equipamentos)


@app.route("/inoperantes")
@exige("ver_painel")
def inoperantes():
    """Mostra os equipamentos inoperantes."""
    equipamentos = repositorio.listar_inoperantes()
    return render_template("inoperantes.html", inoperantes=equipamentos)


@app.route("/equipamentos/novo", methods=["GET", "POST"])
@exige("cadastrar_equipamento")
def cadastrar_equipamento():
    """Cadastra um equipamento."""
    if request.method == "POST":
        try:
            equipamento = Equipamento(
                request.form["patrimonio"], request.form["laboratorio"], request.form["tipo"]
            )
            repositorio.salvar_equipamento(equipamento)
            flash(f"Equipamento {equipamento.patrimonio} cadastrado com sucesso!")
        except ValueError as erro:
            flash(str(erro), "erro")
        return redirect(url_for("cadastrar_equipamento"))

    return render_template("cadastrar_equipamento.html")


@app.route("/chamado/<int:chamado_id>/status", methods=["POST"])
@exige("alterar_status")
def mudar_status(chamado_id):
    """Altera o status de um chamado."""
    try:
        repositorio.atualizar_status(
            chamado_id, request.form["status_resolucao"]
        )
        flash("Status atualizado!")
    except ValueError as erro:
        flash(str(erro), "erro")

    return redirect(url_for("inoperantes"))


@app.route("/historico/<int:equipamento_id>")
@exige("ver_historico")
def historico(equipamento_id):
    """Mostra o histórico de um equipamento."""
    equipamento = repositorio.buscar_equipamento(equipamento_id)
    if equipamento is None:
        flash("Equipamento não encontrado.", "erro")
        return redirect(url_for("inoperantes"))

    chamados = repositorio.historico_equipamento(equipamento_id)
    return render_template("historico.html", equipamento=equipamento, chamados=chamados)


@app.errorhandler(mysql.connector.Error)
def erro_banco(erro):
    return render_template("erro.html", mensagem="Não foi possível acessar o banco de dados. Verifique se o MySQL está ligado e se a senha em conexao.py está correta."), 500


@app.route("/usuarios", methods=["GET", "POST"])
@exige("gerenciar_usuarios")
def usuarios():
    if request.method == "POST":
        try:
            usuario = Usuario(request.form["nome"], request.form["login"], request.form["perfil"])
            usuario.definir_senha(request.form["senha"])
            repositorio.salvar_usuario(usuario)
            flash(f"Usuário {usuario.login} cadastrado com sucesso!")
        except ValueError as erro:
            flash(str(erro), "erro")
        return redirect(url_for("usuarios"))

    return render_template("usuarios.html", usuarios=repositorio.listar_usuarios(),
                           perfis=Usuario.PERFIS_VALIDOS)


if __name__ == "__main__":
    app.run(debug=True)
