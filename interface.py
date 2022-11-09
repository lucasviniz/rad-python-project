import tkinter as tk
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


def executeQuery(tipo, idPessoa, idConta):
    connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")

    if tipo == "pessoa":
        Delete_Line_Pessoa = """DELETE FROM Pessoa WHERE id =  """ + str(idPessoa)
        delete_table(connection, Delete_Line_Pessoa)

    if tipo == "conta":
        Delete_Line_Pessoa = """DELETE FROM Conta WHERE id =  """ + str(idConta)
        delete_table(connection, Delete_Line_Pessoa)

    tk.Label(frameFin, text="DADOS DELETADOS", font=('times', 24, 'italic')).pack();
    connection.close()

def deleteOnelineConta():

    tk.Label(frameX, text="Digite o id da conta que deseja excluir: ").grid(row=0)

    idConta = tk.Entry(frameX)
    idConta.grid(row=0, column=1)
    tipo = "conta"
    idPessoa = "NULL"
    btn = tk.Button(frameX, text="OK", command=lambda: executeQuery(tipo, idPessoa, idConta.get()));
    btn.grid(row=0, column=3)

def deleteOnelinePessoa():

    tk.Label(frameX, text="Digite o id da pessoa que deseja excluir: ").grid(row=0)

    idPessoa = tk.Entry(frameX)
    idPessoa.grid(row=0, column=1)
    tipo = "pessoa"
    idConta = "NULL"
    btn = tk.Button(frameX, text="OK", command=lambda: executeQuery(tipo, idPessoa.get(), idConta));
    btn.grid(row=0, column=3)


def deleteAllconta():
    connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")
    Delete_ALL_pessoa = """DELETE FROM conta """
    delete_table(connection, Delete_ALL_pessoa)
    tk.Label(frameFin, text="DADOS DELETADOS", font=('times', 24, 'italic')).pack();
    connection.close()

def deleteAllpessoa():
    connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")
    Delete_ALL_pessoa = """DELETE FROM Pessoa """
    delete_table(connection, Delete_ALL_pessoa)
    tk.Label(frameFin, text="DADOS DELETADOS", font=('times', 24, 'italic')).pack();
    connection.close()

def excluir():
    tk.Label(frameZ, text="QUAL TABELA DESEJA ALTERAR?", font=('times', 24, 'italic')).pack();


    btn_opcoes1 = tk.Button(frameZ, text="EXCLUIR TODOS OS DADOS DE PESSOA", command= deleteAllpessoa)
    btn_opcoes1.pack(pady=3, padx=15)

    btn_opcoes2 = tk.Button(frameZ, text="EXCLUIR TODOS OS DADOS DE CONTA", command= deleteAllconta)
    btn_opcoes2.pack(pady=3, padx=15)

    btn_opcoes3 = tk.Button(frameZ, text="EXCLUIR UMA LINHA DE PESSOA", command=deleteOnelinePessoa)
    btn_opcoes3.pack(pady=3, padx=15)

    btn_opcoes4 = tk.Button(frameZ, text="EXCLUIR UMA LINHA DE CONTA", command= deleteOnelineConta)
    btn_opcoes4.pack(pady=3, padx=15)
        


def adicionar():
    
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

    tk.Label(frameY, text="DADOS INSERIDOS COM SUCESSO", font=('times', 24, 'italic')).pack();
    
    connection.close()

def inserirDadosPessoa(idU, dado, info):
    connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")
    update_pessoa = """UPDATE Pessoa SET """ + dado + """ = '""" + str(info) + """' WHERE id = """ + str(idU)
    update_table(connection, update_pessoa)
    tk.Label(frameFin, text="ATUALIZAÇÃO EFETUADA", font=('times', 24, 'italic')).pack();
    frameSet.destroy()
    frameX.destroy()
    frameZ.destroy()
    connection.close()

def inserirDadosConta(idU, dado, info):
    connection = create_connection("dbproject", "postgres", "ti123", "127.0.0.1", "5432")
    update_pessoa = """UPDATE Conta SET """ + dado + """ = '""" + info + """' WHERE id = """ + idU
    update_table(connection, update_pessoa)
    tk.Label(frameFin, text="ATUALIZAÇÃO EFETUADA", font=('times', 24, 'italic')).pack();
    frameSet.destroy()
    frameX.destroy()
    frameZ.destroy()
    connection.close()

def inserirIdPessoa(idU, dado):
    tk.Label(frameSet, text="INSIRA O NOVO VALOR:").grid(row=0)
    info = tk.Entry(frameSet)
    info.grid(row=0, column=1)
    print(idU)

    tk.Button(frameSet, text="OK", command=lambda: inserirDadosPessoa(idU, dado, info.get())).grid(row=3, column=1, sticky=tk.W, pady=4)
   
def inserirIdConta(idU, dado):
    tk.Label(frameSet, text="INSIRA O NOVO VALOR:").grid(row=0)
    info = tk.Entry(frameSet)
    info.grid(row=0, column=1)
    print(idU)

    tk.Button(frameSet, text="OK", command=lambda: inserirDadosConta(idU, dado, info.get())).grid(row=3, column=1, sticky=tk.W, pady=4)

def imprimirOpcoesPessoa(veOpcoes):
    
    opcao = veOpcoes.get()
    if opcao == 'CPF':
        print("cpf")
        dado = 'cpf'

    if opcao == 'PRIMEIRO NOME':
        print("primeironome")
        dado = 'primeironome'

    if opcao == 'MEIO NOME':
        print("meionome")
        dado = 'meionome'

    if opcao == 'SOBRENOME':
        print("sobrenome")
        dado = 'sobrenome'

    if opcao == 'IDADE':
        print("idade")
        dado = 'idade'
    
    tk.Label(frameX, text="INFORME O ID DA LINHA POSSUI A INFORMAÇÃO QUE DESEJA ATUALIZAR: ").grid(row=0)

    idU = tk.Entry(frameX)
    idU.grid(row=0, column=1)
    btn = tk.Button(frameX, text="OK", command=lambda: inserirIdPessoa(idU.get(), dado));
    btn.grid(row=0, column=3)


def imprimirOpcoesConta(veOpcoes2):
    opcao = veOpcoes2.get()
    if opcao == 'AGENCIA':
        print("agencia")
        dado = 'agencia'
    if opcao == 'NUMERO':
        print("numero")
        dado = 'numero'
    if opcao == 'SALDO':
        print("saldo")
        dado = 'saldo'
    if opcao == 'GERENTE':
        print("gerente")
        dado = 'gerente'
    if opcao == 'TITULAR':
        print("titular")
        dado = 'titular'

    tk.Label(frameX, text="INFORME O ID DA LINHA POSSUI A INFORMAÇÃO QUE DESEJA ATUALIZAR: ").grid(row=0)

    idU = tk.Entry(frameX)
    idU.grid(row=0, column=1)
    btn = tk.Button(frameX, text="OK", command=lambda: inserirIdConta(idU.get(), dado));
    btn.grid(row=0, column=3)




def editar():
    
    tk.Label(frameZ, text="QUAL TABELA DESEJA ALTERAR?", font=('times', 24, 'italic')).pack();
    

    tk.Label(frameZ,text="PESSOA").pack()
    
    #BOTÃO PESSOA
    listaOpcoes = ["CPF", "PRIMEIRO NOME","MEIO NOME","SOBRENOME", "IDADE"]
    veOpcoes = tk.StringVar()
    veOpcoes.set(listaOpcoes[0])

    op_opcoes = tk.OptionMenu(frameZ, veOpcoes, *listaOpcoes)
    op_opcoes.pack()

    btn_opcoes = tk.Button(frameZ, text="SELECIONAR", command=lambda:[imprimirOpcoesPessoa(veOpcoes)])
    btn_opcoes.pack()
            
    
    #BOTÃO CONTA
    tk.Label(frameZ,text="CONTA").pack()

    listaOpcoes2 = ["AGENCIA", "NUMERO","SALDO","GERENTE", "TITULAR"]
    veOpcoes2 = tk.StringVar()
    veOpcoes2.set(listaOpcoes2[0])

    op_opcoes2 = tk.OptionMenu(frameZ, veOpcoes2, *listaOpcoes2)
    op_opcoes2.pack()

    btn_opcoes2 = tk.Button(frameZ, text="SELECIONAR", command=lambda: [imprimirOpcoesConta(veOpcoes2)])
    btn_opcoes2.pack()



raiz = tk.Tk()

raiz.title("Manipulação do Banco de dados")
raiz.minsize(900, 600)

frame1 = tk.Frame(raiz)
frame1.configure(border=5); frame1.pack()
frame2 = tk.Frame(raiz)
frame2.configure(border=5); frame2.pack()

frameZ = tk.Frame(raiz)
frameZ.configure(border=5); frameZ.pack()

frameX = tk.Frame(raiz)
frameX.configure(border=5); frameX.pack()

frameY = tk.Frame(raiz)
frameY.configure(border=5); frameY.pack()

frameSet = tk.Frame(raiz)
frameSet.configure(border=5); frameSet.pack()

frameFin = tk.Frame(raiz)
frameFin.configure(border=5); frameFin.pack()


tk.Label(frame1, text="O QUE DESEJA FAZER?").pack();


bt1 = tk.Button(frame2, text="ADICIONAR", command=lambda: [adicionar(), frameZ.destroy(), frameX.pack_forget(), frameFin.pack_forget()])
bt1.grid(row=1, column=0, pady=3, padx=15)

bt2 = tk.Button(frame2, text="EDITAR", command=lambda: [editar()]);
bt2.grid(row=1, column=1, pady=3, padx=15)

bt3 = tk.Button(frame2, text="EXCLUIR", command=lambda: [excluir()]);
bt3.grid(row=1, column=2, pady=3, padx=15)

bt4 = tk.Button(frame2, text="SAIR", command=lambda: [raiz.destroy()]);
bt4.grid(row=1, column=3, pady=3, padx=15)

raiz.mainloop()

