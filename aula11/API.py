# IMPORTAÇÃO DA API
import requests #chamar a biblio 

url = "https://rickandmortyapi.com/api/character"  #precisa de uma VARIAVEL para se aguardar um API

resposta = requests.get(url) #esse é o verificador ele te RESPONDE se esta funcionando ou nao
#chamar a variavel dentro do GET
print(resposta) # ele vai responder se esta tudo certo com o LINK/API  




#Consumir a os dados da  API
json = resposta.json()
# com esse codigo ele vai transmitir as informações da API como jsaon
print(json)



# Acesso ao result
personagem = json["results"] #chamar uma variavel com results 
print(personagem)



#laço  de reptição para consultar nomes 
for nome_personagem in personagem:
    print(nome_personagem["name"]) #ACESSO A INFORMÇÕES DOS PERSONAGEM/ NOMES, ROUPAS, ESPECIE ETC
    
    
    
    
    # EXEMPLOS PRATICOS 01
    
     #Mostra de forma organizada, mostra o primeiro nome, status e a especie de TODOS OS PERSONAS USANDO O LAÇO DE REPRETIÇÃO "REPEAT"
for mais_info in personagem:
    print("Nome: ", mais_info["name"])  # chamar nome de chaves 
    print("status:",mais_info["status"])
    print("especie:", mais_info["species"])
    print("--------------------------") #para separar as informações





#   EXEMPLOS PRATICOS 02

id = int(input("Digite um numero int:"))

#DEIXAR AS INFOS DA API MAIS FELXIVEL
link_API = f"https://rickandmortyapi.com/api/character/{id}" #modifica o codigo, e consegue passar variavel (demonstrado no final da URL)

resposta = requests.get(link_API) #consultar a API
json_novo = resposta.json() # chama a API


print("Nome: ", json_novo["name"])  # chamar nome de chaves 
print("status:",  json_novo["status"])
print("especie:", json_novo["species"])
print("--------------------------")














