
from flask import Flask, render_template, request, redirect, url_for, flash
import repositorio

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
        flash("Chamado recebido com sucesso!")
        return redirect(url_for("inoperantes"))

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
        flash("Equipamento recebido com sucesso!")
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
    chamados = repositorio.historico_equipamento(equipamento_id)
    return render_template("historico.html", chamados=chamados)


if __name__ == "__main__":
    app.run(debug=True)
