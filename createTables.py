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


def create_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Tabela criada com sucesso!")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")


table_Pessoa_query = """CREATE TABLE Pessoa(
    id SERIAL PRIMARY KEY,
    cpf char(17),
    primeiroNome varchar(50) NOT NULL,
    meioNome varchar(50),
    sobrenome varchar(50) NOT NULL,
    cargo varchar(50),
    idade int CONSTRAINT idade_positiva CHECK (idade >= 0),
    conta int
)
"""

table_Conta_query = """CREATE TABLE Conta(
    id SERIAL PRIMARY KEY,
    agencia varchar(8) NOT NULL,
    numero varchar(9) NOT NULL,
    saldo float NOT NULL,
    gerente varchar(50),
    titular int
)
"""

table_Usuario_query = """CREATE TABLE Usuario(
    id SERIAL PRIMARY KEY,
    email varchar(100),
    login varchar(9),
    senha varchar(50),
    pessoa_id int,
    FOREIGN KEY(pessoa_id) REFERENCES Pessoa(id)
)
"""

create_table(connection, table_Pessoa_query)
create_table(connection, table_Usuario_query)
create_table(connection, table_Conta_query)


connection.close()