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

def update_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Dados atualizados com sucesso!")
        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")

x = input("QUAL TABELA DESEJA ALTERAR?  1- PESSOA   2- CONTA\n")
if x == '1':
    opcao = input("QUAL COLUNA DESEJA ATUALIZAR?\n1 - CPF\n2 - PRIMEIRO NOME\n3 - MEIO NOME\n4 - SOBRENOME\n5 - IDADE\n6 - SAIR\n")
    if opcao == '1':
        dado = 'cpf'
    if opcao == '2':
        dado = 'primeironome'
    if opcao == '3':
        dado = 'meionome'
    if opcao == '4':
        dado = 'sobrenome'
    if opcao == '5':
        dado = 'idade'
        
    if opcao >= '1' and opcao<='5':
        idU = input("INFORME O ID DA LINHA POSSUI A INFORMAÇÃO QUE DESEJA ATUALIZAR: ")
        info = input("INSIRA O NOVO VALOR: ")
        update_pessoa = """UPDATE Pessoa SET """ + dado + """ = '""" + info + """' WHERE id = """ + idU
        update_table(connection, update_pessoa)


if x == '2':
    opcao = input("QUAL COLUNA DESEJA ATUALIZAR?\n1 - AGENCIA\n2 - NUMERO\n3 - SALDO\n4 - GERENTE\n5 - TITULAR\n6 - SAIR\n")
    if opcao == '1':
        dado = 'agencia'
    if opcao == '2':
        dado = 'numero'
    if opcao == '3':
        dado = 'saldo'
    if opcao == '4':
        dado = 'gerente'
    if opcao == '5':
        dado = 'titular'

    if opcao >= '1' and opcao<='5':
        idU = input("INFORME O ID DA LINHA POSSUI A INFORMAÇÃO QUE DESEJA ATUALIZAR: ")
        info = input("INSIRA O NOVO VALOR: ")
        update_pessoa = """UPDATE Conta SET """ + dado + """ = '""" + info + """' WHERE id = """ + idU
        update_table(connection, update_pessoa)
