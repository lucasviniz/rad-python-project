import psycopg2
from psycopg2 import OperationalError 
import os

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port)
        print("Conexão com o banco ", db_name, " foi bem sucedida")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")
    return connection

def insert_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Valores inseridos com sucesso!")
        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

def create_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Tabela criada com sucesso!")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")


def update_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Dados atualizados com sucesso!")
        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")


def delete_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Dados deletados com sucesso!")
        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")