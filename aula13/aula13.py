# PYTHON X BANCO DE DADOS

import pymysql as pySQL  #import 



#conexão com o banco de dados
conexao = pySQL.connect(
    host="localhost",        # endereço do servidor
    user="root",      # usuário do MySQL
    password="",    # senha do MySQL
    database="bd_livrariaonline",# nome do banco já criado
    port=3306                # porta padrão
)




# criar cursor - versão dicionario, o cursor conversa com o banco (manda e recebe dados)
cursor = conexao.cursor(pySQL.cursors.DictCursor) #recomendado




#buscar resistros
cursor.execute("SELECT * FROM clientes") #"POR FAVOR EXECUTE O "SELECT BLA BLA""
todos = cursor.fetchall() #quantidades de informaçoes q eu quero RETORNAR




for cliente in todos: #retornar resultado 
    print(cliente["nome"],"-", cliente["email"],"-", cliente["telefone"]) #resultado organizado
    
    
    
