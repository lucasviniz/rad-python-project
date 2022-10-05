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

connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")



try:
    os.mkdir('./ArquivosTemporarios')
except OSError as e:
    print(f"O erro '{e}' ocorreu")



with open('dados/nomes.txt','r') as inFile, \
     open('ArquivosTemporarios/nomes.temp.txt', 'w') as outFile:

    for line in inFile:
        if not line.endswith(';', -2, len(line) - 1):
            line = line.rstrip() + "')\n"
            frase = line.split(" ")
            dado ="','".join(frase)
        outFile.write(dado)
        table_insert_pessoa = """INSERT INTO Pessoa (cpf, primeiroNome, meioNome, sobrenome, idade, conta)
VALUES ('
"""
        sql = table_insert_pessoa+dado
        insert_table(connection, sql)


with open('dados/contas.txt','r') as inFile, \
     open('ArquivosTemporarios/contas.temp.txt', 'w') as outFile:

    for line in inFile:
        if not line.endswith(';', -2, len(line) - 1):
            line = line.rstrip() + "')\n"
            frase = line.split(" ")
            dado ="','".join(frase)
        outFile.write(dado)
        table_insert_conta = """INSERT INTO Conta (agencia, numero, saldo, gerente, titular)
VALUES ('
"""
        sql = table_insert_conta+dado
        insert_table(connection, sql)

connection.close()