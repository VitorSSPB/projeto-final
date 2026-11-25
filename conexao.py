import mysql.connector

CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "controle_lab",
}


def conectar():
    return mysql.connector.connect(**CONFIG)
