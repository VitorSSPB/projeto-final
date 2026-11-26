
import mysql.connector

CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "Z1x2c3v4",
    "database": "controle_lab"
}


def conectar():
    """Conecta ao banco de dados MySQL."""
    try:
        return mysql.connector.connect(**CONFIG)
    except mysql.connector.Error as erro:
        print("Erro ao conectar com o MySQL:", erro)
        raise
