from urllib.request import OpenerDirector
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

def select_table_pessoa(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Consulta feita com sucesso!")

        lista_consulta = cursor.fetchall()
        with open('ArquivosConsulta/ConsultaCompleta/pessoa.txt','w') as outFile:
            for linha in lista_consulta:
                outFile.write(str(linha[0])+"  "+str(linha[1]).strip()+"  "+str(linha[2])+"  "+str(linha[3])+"  "+str(linha[4])+"  "+str(linha[5])+"  "+str(linha[6])+"\n")
                print(linha)

        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")


def select_table_one_pessoa(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Consulta feita com sucesso!")

        lista_consulta = cursor.fetchall()
        i = 0
        with open('ArquivosConsulta/ConsultaUnica/pessoa.txt','a') as outFile:
            for linha in lista_consulta:
                print("ID: ", linha[0])
                print("CPF: ", linha[1].strip())
                print("Primeiro nome: ", linha[2])
                print("Nome do meio: ", linha[3])
                print("Sobrenome: ", linha[4])
                print("Idade: ", linha[5])
                print("Conta: ", linha[6])
                outFile.write("CONSULTA\n")
                outFile.writelines("  ID: "+str(linha[0]) + "\n" "  CPF: " + str(linha[1]).strip() + "\n" + "  PRIMEIRO NOME: " + str(linha[2]) + "\n" + "  MEIONOME: " + str(linha[3]) + "\n" + "  SOBRENOME: " + str(linha[4]) + "\n" + "  IDADE: " + str(linha[5]) + "\n" + "  CONTA: " + str(linha[6]) + "\n\n\n")

        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")




def select_table_conta(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Consulta feita com sucesso!")

        lista_consulta = cursor.fetchall()
        with open('ArquivosConsulta/ConsultaCompleta/conta.txt','w') as outFile:
            for linha in lista_consulta:
                outFile.write(str(linha[0])+"  "+str(linha[1]).strip()+"  "+str(linha[2])+"  "+str(linha[3])+"  "+str(linha[4])+"  "+str(linha[5])+"  "+str(linha[6])+"\n")
                print(linha)

        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")


def select_table_one_conta(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Consulta feita com sucesso!")

        lista_consulta = cursor.fetchall()
        i = 0
        with open('ArquivosConsulta/ConsultaUnica/conta.txt','a') as outFile:
            for linha in lista_consulta:
                print("ID: ", linha[0])
                print("CPF: ", linha[1].strip())
                print("Primeiro nome: ", linha[2])
                print("Nome do meio: ", linha[3])
                print("Sobrenome: ", linha[4])
                print("Idade: ", linha[5])
                print("Conta: ", linha[6])
                outFile.write("CONSULTA\n")
                outFile.writelines("  ID: "+str(linha[0]) + "\n" "  CPF: " + str(linha[1]).strip() + "\n" + "  PRIMEIRO NOME: " + str(linha[2]) + "\n" + "  MEIONOME: " + str(linha[3]) + "\n" + "  SOBRENOME: " + str(linha[4]) + "\n" + "  IDADE: " + str(linha[5]) + "\n" + "  CONTA: " + str(linha[6]) + "\n\n\n")

        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")

try:
    os.makedirs('./ArquivosConsulta/ConsultaCompleta') or os.makedirs('./ArquivosConsulta/ConsultaUnica')
except OSError as e:
    print(f"O erro '{e}' ocorreu")



x=input("O QUE DESEJA CONSULTA?\n1 - TODA A TABELA PESSOA\n2 - TODA A TABELA CONTA\n3 - SOMENTE UMA LINHA DA TABELA PESSOA\n4 - SOMENTE UMA LINHA DA TABELA CONTA\n")



if x=='1':
    table_consulta_pessoa = """SELECT * FROM Pessoa"""
    select_table_pessoa(connection, table_consulta_pessoa)
if x=='2':
    table_consulta_conta = """SELECT * FROM Pessoa"""
    select_table_conta(connection, table_consulta_conta)

if x=='3':
    cpf=input("INFORME O SEU CPF: ")
    table_consulta_pessoa = """SELECT * FROM Pessoa WHERE cpf = '\n""" + cpf + "  '"
    select_table_one_pessoa(connection, table_consulta_pessoa)

if x=='4':
    numConta=input("INFORME O SEU CPF: ")
    table_consulta_pessoa = """SELECT * FROM Pessoa WHERE cpf = '\n""" + numConta + "  '"
    select_table_one_conta(connection, table_consulta_pessoa)

connection.close()