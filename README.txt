Para que o programa funcione corretamente, os arquivos deveram ser executados na seguinte ordem:
AS PRINCIPAIS ETAPAS É NECESSARIO SER EXECUTADAS NA ORDEM: 
	1- connect.py (cria e faz a conexão com banco de dados, no caso o postgreSQL)
	2- createTables.py (cria a tabela pessoa e a tabela conta no banco de dados)
	3- insertTables.py (insere os dados retirados do arquivo, no caso arquivos utilizados da pasta dados) 

O RESTANTE DOS ARQUIVOS É PARA A ATUALIZAÇÃO, REMOÇÃO E CONSULTA NO BANCO DE DAODS: 
	1- updateTable.py (para a atualização de dados)
	2- deleteTable.py (para a remoção de dados)
	3- queryTable.py  (para a consulta de dados)
