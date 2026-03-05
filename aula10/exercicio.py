#Salvar cadastro

nome = input("Digite o seu nome")
idade = input("Digite a sua idade")

open("salvamento.txt", "w")
 
#salvar arquivos

with open("salvamento.txt", "w") as arquivo:
    arquivo.write(f"Nome: {nome}\n")  #Esse modelo para mostrar as informaçoes do cliente para o arquivo
    arquivo.write(f"Idade: {idade}\n") #

   
