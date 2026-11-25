from flask import Flask, render_template, request, redirect, url_for, flash
import repositorio
from models import Chamado, Equipamento

app = Flask(__name__)
app.secret_key = "controle-equipamentos-etec"


@app.route("/")
def inicio():
    """Abre a página inicial."""
    return redirect(url_for("inoperantes"))


@app.route("/abrir", methods=["GET", "POST"])
def abrir_chamado():
    """Abre um novo chamado."""
    if request.method == "POST":
        try:
            chamado = Chamado(request.form["equipamento_id"], request.form["descricao_problema"])
            repositorio.salvar_chamado(chamado)
            flash("Chamado aberto com sucesso!")
            return redirect(url_for("inoperantes"))
        except ValueError as erro:
            flash(str(erro))

    equipamentos = repositorio.listar_equipamentos()
    return render_template("abrir_chamado.html", equipamentos=equipamentos)


@app.route("/inoperantes")
def inoperantes():
    """Mostra os equipamentos inoperantes."""
    equipamentos = repositorio.listar_inoperantes()
    return render_template("inoperantes.html", inoperantes=equipamentos)


@app.route("/equipamentos/novo", methods=["GET", "POST"])
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
            flash(str(erro))
        return redirect(url_for("cadastrar_equipamento"))

    return render_template("cadastrar_equipamento.html")


@app.route("/chamado/<int:chamado_id>/status", methods=["POST"])
def mudar_status(chamado_id):
    """Altera o status de um chamado."""
    try:
        repositorio.atualizar_status(
            chamado_id, request.form["status_resolucao"]
        )
        flash("Status atualizado!")
    except ValueError as erro:
        flash(str(erro))

    return redirect(url_for("inoperantes"))


@app.route("/historico/<int:equipamento_id>")
def historico(equipamento_id):
    """Mostra o histórico de um equipamento."""
    equipamento = repositorio.buscar_equipamento(equipamento_id)
    if equipamento is None:
        flash("Equipamento não encontrado.")
        return redirect(url_for("inoperantes"))

    chamados = repositorio.historico_equipamento(equipamento_id)
    return render_template("historico.html", equipamento=equipamento, chamados=chamados)


if __name__ == "__main__":
    app.run(debug=True)
