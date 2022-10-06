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

def delete_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Dados deletados com sucesso!")
        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")


connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")


x=input("O que deseja fazer?\n1 - EXCLUIR TODOS OS DADOS DE PESSOA\n2 - EXCLUIR TODOS OS DADOS DE CONTA\n3 - EXCLUIR UMA LINHA DE PESSOA\n4 - EXCLUIR UMA LINHA DE CONTA\n")

if x == '1':
    Delete_ALL_pessoa = """DELETE FROM Pessoa """
    delete_table(connection, Delete_ALL_pessoa)

if x == '2':
    Delete_ALL_pessoa = """DELETE FROM conta """
    delete_table(connection, Delete_ALL_pessoa)

if x == '3':
    idPessoa = input("Digite o id da pessoa que deseja excluir: ")
    Delete_Line_Pessoa = """DELETE FROM Pessoa WHERE id =  """ + idPessoa
    delete_table(connection, Delete_Line_Pessoa)

if x == '4':
    idConta = input("Digite o id da conta que deseja excluir: ")
    Delete_Line_Pessoa = """DELETE FROM Conta WHERE id =  """ + idConta
    delete_table(connection, Delete_Line_Pessoa)


connection.close()
