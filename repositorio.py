
import mysql.connector

from conexao import conectar
from models import Equipamento, Chamado


def listar_equipamentos():
    """Lista os equipamentos cadastrados."""
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM equipamento ORDER BY laboratorio, patrimonio")
    linhas = cur.fetchall()
    con.close()

    return [Equipamento(l["patrimonio"], l["laboratorio"], l["tipo"], l["id"]) for l in linhas]


def salvar_equipamento(equipamento):
    """Salva um equipamento."""
    con = conectar()
    cur = con.cursor()

    try:
        cur.execute(
            "INSERT INTO equipamento (patrimonio, laboratorio, tipo) VALUES (%s, %s, %s)",
            (equipamento.patrimonio, equipamento.laboratorio, equipamento.tipo)
        )
        con.commit()
    except mysql.connector.IntegrityError:
        raise ValueError("Patrimônio já cadastrado.")
    finally:
        con.close()


def salvar_chamado(chamado):
    """Salva um chamado."""
    con = conectar()
    cur = con.cursor()

    cur.execute(
        "INSERT INTO chamado (equipamento_id, data, descricao_problema, status_resolucao) VALUES (%s, %s, %s, %s)",
        (chamado.equipamento_id, chamado.data, chamado.descricao_problema, chamado.status_resolucao)
    )

    con.commit()
    con.close()


def listar_inoperantes():
    """Lista os equipamentos com chamados não resolvidos."""
    con = conectar()
    cur = con.cursor(dictionary=True)

    cur.execute("""
        SELECT c.id AS chamado_id, e.id AS equipamento_id, e.patrimonio,
        e.laboratorio, e.tipo, c.descricao_problema, c.status_resolucao, c.data
        FROM chamado c
        JOIN equipamento e ON e.id = c.equipamento_id
        WHERE c.status_resolucao <> 'Resolvido'
        ORDER BY c.data
    """)

    linhas = cur.fetchall()
    con.close()
    return linhas


def buscar_chamado(chamado_id):
    """Busca um chamado pelo ID."""
    con = conectar()
    cur = con.cursor(dictionary=True)
    cur.execute("SELECT * FROM chamado WHERE id = %s", (chamado_id,))
    l = cur.fetchone()
    con.close()

    if l is None:
        return None

    return Chamado(l["equipamento_id"], l["descricao_problema"],
                   l["data"], l["status_resolucao"], l["id"])


def atualizar_status(chamado_id, novo_status):
    """Atualiza o status de um chamado."""
    chamado = buscar_chamado(chamado_id)

    if chamado is None:
        raise ValueError("Chamado não encontrado.")

    chamado.alterar_status(novo_status)

    con = conectar()
    cur = con.cursor()
    cur.execute(
        "UPDATE chamado SET status_resolucao = %s WHERE id = %s",
        (chamado.status_resolucao, chamado.id)
    )
    con.commit()
    con.close()


def historico_equipamento(equipamento_id):
    """Lista o histórico de chamados de um equipamento."""
    con = conectar()
    cur = con.cursor(dictionary=True)

    cur.execute("""
        SELECT c.id, c.data, c.descricao_problema, c.status_resolucao,
        e.patrimonio, e.laboratorio
        FROM chamado c
        JOIN equipamento e ON e.id = c.equipamento_id
        WHERE e.id = %s
        ORDER BY c.data DESC
    """, (equipamento_id,))

    linhas = cur.fetchall()
    con.close()
    return linhas
