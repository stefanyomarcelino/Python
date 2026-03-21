# AQ OA ARQUIVOS DESTINADO A TRABALHAR COM BANCO DE DADOS FAZER AS OPERAÇOES UPDATES, INSERT E DELETE

# PYTHON X BANCO DE DADOS

import pymysql as pySQL  #import 



#conexão com o banco de dados
conexao = pySQL.connect(
    host="localhost",        # endereço do servidor
    user="root",      # usuário do MySQL
    password="",    # senha do MySQL
    database="bd_livrariaonline",# nome do banco já criado
    port=3306                # porta padrão
)  #sempre que for mexer com SQL precisa importar os codigos

cursor = conexao.cursor(pySQL.cursors.DictCursor) #recomendado  #cursor é a TROCA PARA O BANCO DE DADOS




try: #PARA VERIFICAR SE A OPERAÇÃO DEU CERTO OU NÃO, caso não, ele vai dar erro
    sql_insert = "INSERT INTO cliente (nome, email) VALUES (%s, %s)" 
    cursor.execute(sql_insert, ("anna", "Ana@gmail.com"))
    conexao.commit()
    print("Inserido com sucesso! ID:", cursor.lastrowid) # RETORNA UM ID criado

except Exception as erro:
    conexao.rollback()
    print("Erro! Operação revertida:", erro)

finally:
    cursor.close()
    conexao.close() #fechar a conexão com o banco de dados






#UPDATE: ele atualizar o dado que ja existe
try:
    sql_update = "UPDATE cliente SET email = %s WHERE id_cliente = %s"
    cursor.execute(sql_update, ("novo@email.com", 1)) #digite o novo email
    conexao.commit()  # CONFIRMA O UPDATE
    print("Linhas afetadas:", cursor.rowcount)

except Exception as erro:
    conexao.rollback()  # desfaz tudo se algo der errado e quantas linhas foram afetas 
    print("Erro! Operação revertida:", erro)




#CODIGO PARA DELETAR


# cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (5))
# conexao.commit() #confirma o delete

# except Exception as erro:
#     conexao.rollback()
#     print("erro! operação revertida", erro)

# finally:
#     cursor.close
#     conexao.close()   # ELE NAO DELETA PQ É UM FOREING KEY E SE FOR DELETADA NOSSO SQL QUEBRA (significa que é um codigo forte)
    
    
    
# CODIGO 2 PQ O DE CIMA TA DANDO ERRO 

# try:
#     cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (5,))
#     conexao.commit()  # confirma o delete
#     print("Registro deletado com sucesso!")

# except Exception as erro:
#     conexao.rollback()
#     print("Erro! Operação revertida:", erro)

# finally:
#     cursor.close()
#     conexao.close()
