#Criar um Menu

# Data da entrega: 15/03/2025

# Criar um menu para selecao
# 1 - Consultar por ID
# 2 - Consultar por nome
# 3 - Lista de personagens

# se for opcao 1:
"""
    Pedir ao usuario para digitar um ID(Numero inteiro) e retornar de dentro da API o personagem referente ao ID digitado
    Retorne todas as informações sobre o personagem
"""

# Se selecionar a opcao 2:
"""
    Pedir ao usuario para digitar nome e retornar o resultado

    OBS de codigo: para percorrer o json e retornar o nome digitado.
"""
    # for personagem in dados["results"]:
    #     print(personagem["name"])



# Se selecionar a opcao 3:
# Retornar todos os personagens
# Lista das informações que deverão ser retornadas:
"""
"results": [
"id":
"name":
"status":
"species":
"gender":
]
"origin": {
    "name": "Earth (C-137)",
},
"location": {
    "name": "Citadel of Ricks",
},
"image": "https://rickandmortyapi.com/api/character/avatar/1.jpeg",
"""


#ATIVIDADE A BAIXO ⬇️

# Criação de um MENU

import requests #chamada da biblio

url = "https://rickandmortyapi.com/api/character"
resposta = requests.get(url)
print(resposta)

while True:
    

   #Solicitar os dados do usuario


    nome = input("Digite o seu nome")
    print("Ola bem-vindo", nome)
    print("Aqui você pode pesquisar informações sobre a serie")
    print("") #para separar as informações
    print ("Escolha uma das opções a baixo ⬇️")




    #Opções para o usuario
    print("1 - Opção 1: Inforções do personagem ")
    print("--------------------------") #para separar as informações
    print("2 - Opção 2: Nome personagem ")
    print("--------------------------") #para separar as informações
    print("3 - Opção 3 Lista completas de informações dos personagens")
    print("") #para separar as informações




    opção = input("Digite o numero da opção:").strip()

    if opção == "1":
        print("Você escolheu a PRIMEIRA opção: Por favor", nome, "digite um ID" ) 
            
        Usuario = int(input("Digite um ID"))
        link_API = f"https://rickandmortyapi.com/api/character/{Usuario}"

        resposta = requests.get(link_API) 
        json = resposta.json() 

        print("Nome: ", json ["name"])
        print("")
        
        



        
    elif opção == "2":
        print("Você escolheu a SEGUNDA opção: Por favor", nome, "Digite um NOME")

        persona_nome = input("Digite o nome de um personagem: ").strip()
        api = f"https://rickandmortyapi.com/api/character?name={persona_nome}"

        resposta = requests.get(api)

        if resposta.status_code == 200: #caso esteja funcionando o link
            data = resposta.json()              
            resultados = data.get("results", [])
            if resultados:
                p = resultados[0]                # pega o primeiro resultado
                print("Nome:", p.get("name"))
                print("--------------------------")
                print("Specie:", p.get("species"))
                print("--------------------------")
                print("Gender:", p.get("gender"))
                print("--------------------------")
                print("status:", p.get("status"))
            
            

        
            
    elif opção == "3":
        print("Você escolheu a TERCEIRA opção: Por favor", nome, "Solicitar retorno da lista de personagens")
        
        retorno = input("Digite para solicitar retorno").strip()
        ipa = f"https://rickandmortyapi.com/api/character" #chamar a API

        resposta = requests.get(ipa) # Fazer o request

        json = resposta.json() #Chamar o json (modelo)

        personagens = json["results"] # result para poder fazer a lista

        for dados in personagens:
            print("------------------------------")
            print("ID:", dados["id"])
            print("Nome:", dados["name"])
            print("Status:", dados["status"])
            print("Espécie:", dados["species"])
            print("Gênero:", dados["gender"])
            print("Origem:", dados["origin"]["name"])
            print("Localização:", dados["location"]["name"])
            print("Imagem:", dados["image"])

    #nome percorrendo todos os personagens 
    
    else:
        print("Opção inválida! essa opção não existe! coloque apenas uma das 3 opções solicitadas a cima")
            
    
 
    

#retorno pro menu 
    escolha_1 = input("Voltar ao menu Sim ou Nao: ").lower()
    if escolha_1 != "sim": 
        print("Saida")
        break







    
    
    
    
    

    