#MANIPULAÇÃO RAPIDA DE UM BANCO DE DADOS
Para que o programa funcione corretamente, os arquivos deveram ser executados na seguinte ordem:
AS PRINCIPAIS ETAPAS É NECESSARIO SER EXECUTADAS NA ORDEM: 
	1- connect.py (cria e faz a conexão com banco de dados, no caso o postgreSQL)
	2- createTables.py (cria a tabela pessoa e a tabela conta no banco de dados)
	3- insertTables.py (insere os dados retirados do arquivo, no caso arquivos utilizados da pasta dados) 

O RESTANTE DOS ARQUIVOS É PARA A ATUALIZAÇÃO, REMOÇÃO E CONSULTA NO BANCO DE DAODS: 
	1- updateTable.py (para a atualização de dados)
	2- deleteTable.py (para a remoção de dados)
	3- queryTable.py  (para a consulta de dados)

*NOVA ATUALIZAÇÃO
Todos os arquivos continuam conforme apresentados anteriormente
Agora dentre os principais arquivos, o "createtables.py" deverá ser executado anteriormente para que o componente a seguir siga funcionando normalmente

-UM NOVO COMPONENTE ARQUIVO FOI ADICIONADO "INTERFACE.PY" UTILIZANDO A BIBLIOTECA PADRÃO TKINTER

O Programa possui 4 botões:
-ADICIONAR
-EDITAR
-EXCLUIR
-SAIR
Cada um realiza a função que o seu proprio nome ja deixa evidente

Para que o programa rode sem complicações é necessario que a cada iteração o programa seja fechado e aberto novamente 
EX: ao clicar no botão "ADICIONAR" o programa irá responder a sua requisição porém você poderá ter complicações caso tente fazer uma requisição novamente
**RECOMENDO SEMPRE QUE FECHE O PROGRAMA AO FINAL DE CADA ATO E ABRA NOVAMENTE**

o programa é simples e sensivel tenha cuidado com ele.
