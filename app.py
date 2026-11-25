
from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, flash
import repositorio

app = Flask(__name__)
app.secret_key = "controle-equipamentos-etec"

EQUIPAMENTOS_EXEMPLO = [
    {"id": 1, "patrimonio": "PAT-0001", "laboratorio": "Laboratório 1", "tipo": "Computador"},
    {"id": 2, "patrimonio": "PAT-0002", "laboratorio": "Laboratório 1", "tipo": "Monitor"},
    {"id": 3, "patrimonio": "PAT-0105", "laboratorio": "Laboratório 2", "tipo": "Computador"},
    {"id": 4, "patrimonio": "PAT-0106", "laboratorio": "Laboratório 2", "tipo": "Impressora"},
    {"id": 5, "patrimonio": "PAT-0210", "laboratorio": "Laboratório 3", "tipo": "Projetor"},
]

INOPERANTES_EXEMPLO = [
    {"patrimonio": "PAT-0105", "laboratorio": "Laboratório 2", "tipo": "Computador",
     "descricao_problema": "PC 05 sem internet", "status_resolucao": "Em andamento",
     "data": datetime(2026, 11, 3, 8, 30)},
    {"patrimonio": "PAT-0002", "laboratorio": "Laboratório 1", "tipo": "Monitor",
     "descricao_problema": "Monitor piscando e desligando sozinho", "status_resolucao": "Aberto",
     "data": datetime(2026, 11, 4, 10, 15)},
    {"patrimonio": "PAT-0106", "laboratorio": "Laboratório 2", "tipo": "Impressora",
     "descricao_problema": "Papel atolando em toda impressão", "status_resolucao": "Aberto",
     "data": datetime(2026, 11, 4, 14, 0)},
]


@app.route("/")
def inicio():
    return redirect(url_for("inoperantes"))


@app.route("/abrir", methods=["GET", "POST"])
def abrir_chamado():
    if request.method == "POST":
        print("Chamado recebido:", dict(request.form))
        flash("Chamado recebido com sucesso!")
        return redirect(url_for("inoperantes"))

    return render_template("abrir_chamado.html", equipamentos=EQUIPAMENTOS_EXEMPLO)


@app.route("/inoperantes")
def inoperantes():
    return render_template("inoperantes.html", inoperantes=INOPERANTES_EXEMPLO)


@app.route("/equipamentos/novo", methods=["GET", "POST"])
def cadastrar_equipamento():
    if request.method == "POST":
        print("Equipamento recebido:", dict(request.form))
        flash("Equipamento recebido com sucesso!")
        return redirect(url_for("cadastrar_equipamento"))

    return render_template("cadastrar_equipamento.html")


@app.route("/chamado/<int:chamado_id>/status", methods=["POST"])
def mudar_status(chamado_id):
    try:
        repositorio.atualizar_status(
            chamado_id,
            request.form["status_resolucao"]
        )
        flash("Status atualizado!")

    except ValueError as erro:
        flash(str(erro))

    return redirect(url_for("inoperantes"))


@app.route("/historico/<int:equipamento_id>")
def historico(equipamento_id):
    chamados = repositorio.historico_equipamento(equipamento_id)

    return render_template("historico.html", chamados=chamados)


if __name__ == "__main__":
    app.run(debug=True)
