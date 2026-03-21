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
cursor = conexao.cursor(pySQL.cursors.DictCursor) #recomendado  #cursor é a TROCA PARA O BANCO DE DADOS




#buscar resistros
cursor.execute("SELECT * FROM clientes") #"POR FAVOR EXECUTE O "SELECT BLA BLA""
todos = cursor.fetchall() #quantidades de informaçoes q eu quero RETORNAR




# for cliente in todos: #retornar resultado 
#     print(cliente["nome"],"-", cliente["email"],"-", cliente["telefone"]) #resultado organizado
    
    
    


# DIA 20/03

cursor.execute("SELECT * FROM clientes WHERE id_cliente = 1") #executar no banco de dados  #vc pode usar para retornar dados para o usuario 

cliente = cursor.fetchone() #trazer para o python em sua linguagem 


print(cliente)



# buscar com filtro seguro e dinamico

# nome_bucs = "anna zousa" #string chumbada para pesquisa
# cursor.execute("SELECT * FROM cliente WHERE nome LIKE = %s", (nome_bucs,)) #precisa pesquisar e retornar como duplas


# resultado = cursor.fetchall() #retornar resultados com FETCH 


# print(resultado)

