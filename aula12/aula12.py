import pandas as pd # pandas -> pd
 
nome = str(input("Digite seu nome: ")) # str -> texto
idade = input("Digite sua idade: ") # int -> numero inteiro
altura = float(input("Digite sua altura: ")) # float-> ponto flutuante
 
# Criação de um dicionário para receber os dados digitados pelo usuário
 
dados = {
    "nome": [nome],
    "idade": [idade],
    "altura": [altura]
}
 
# # DataFrame -> é a criação de um xcel em um formato que o pandas entende para trabalhar com dados
 
excel = pd.DataFrame(dados)
 
#to_excel() -> serve para criar uma nova planilha, pegar os dados digitados pelo usuário em formato DataFrame e gravar os dados na planilha criada
 
excel.to_excel("aula12/cadastro_aluno.xlsx" , index=False)
 
# LOC > NUMERO DA LINHA / NOME DA COLUNA
 
# Ler o excel
 
leitura_excel = pd.read_excel("aula12/cadastro_aluno.xlsx", dtype={"idade":str})  #LEITURA DE EXECEL
nova_linha = len(leitura_excel) # LEN -> conta quantas linhas existem no excel e cria uma nova linha para receber a nova informação digitada pelo usuáriom
 
leitura_excel.loc[nova_linha, "nome"] = dados["nome"]
leitura_excel.loc[nova_linha, "idade"] = dados["idade"] #Ultilizar o LOC para criar um novo dedo ou ALTERAR um novo dado
leitura_excel.loc[nova_linha, "altura"] = dados["altura"]
 

leitura_excel.to_excel("aula12/cadastro_aluno.xlsx" , index=False)

#print(leitura_excel["nome"])
 
leitura_excel = leitura_excel.drop(2)
 
leitura_excel.loc[2, "nome"] = dados["nome"]
leitura_excel.loc[2, "idade"] = dados["idade"]
leitura_excel.loc[2, "altura"] = dados["altura"]
 
# salvar
leitura_excel.to_excel("aula12/cadastro_aluno.xlsx" , index=False)


 
 




 