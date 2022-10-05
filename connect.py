import psycopg2
from psycopg2 import OperationalError

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

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executada com sucesso")
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

# Conexão com o banco de dados default
connection = create_connection("postgres", "postgres", "ti123", "127.0.0.1", "5432")

create_database_query = "CREATE DATABASE dbproject"
create_database(connection, create_database_query)

connection.close()