import mysql.connector

from conexao import conectar
from models import Equipamento, Chamado


def listar_equipamentos():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM equipamento ORDER BY laboratorio, patrimonio")
    linhas = cur.fetchall()
    con.close()
    return [Equipamento(l["patrimonio"], l["laboratorio"], l["tipo"], l["id"]) for l in linhas]


def salvar_equipamento(equipamento):
    con = conectar()
    cur = con.cursor()
    try:
        cur.execute(
            "INSERT INTO equipamento (patrimonio, laboratorio, tipo) VALUES (%s, %s, %s)",
            (equipamento.patrimonio, equipamento.laboratorio, equipamento.tipo),
        )
        con.commit()
    except mysql.connector.IntegrityError:
        raise ValueError(f"O patrimônio {equipamento.patrimonio} já está cadastrado.")
    finally:
        con.close()


def salvar_chamado(chamado):
    con = conectar()
    cur = con.cursor()
    cur.execute(
        "INSERT INTO chamado (equipamento_id, data, descricao_problema, status_resolucao) "
        "VALUES (%s, %s, %s, %s)",
        (chamado.equipamento_id, chamado.data, chamado.descricao_problema, chamado.status_resolucao),
    )
    con.commit()
    con.close()


def listar_inoperantes():
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute(
        "SELECT c.id AS chamado_id, e.id AS equipamento_id, e.patrimonio, e.laboratorio, e.tipo, "
        "c.descricao_problema, c.status_resolucao, c.data "
        "FROM chamado c JOIN equipamento e ON e.id = c.equipamento_id "
        "WHERE c.status_resolucao <> 'Resolvido' "
        "ORDER BY c.data"
    )
    linhas = cur.fetchall()
    con.close()
    return linhas
