#Salvar cadastro

open("cadastro.txt", "w")

#Perguntar o nome
with open("cadastro.txt", "w") as arquivo:
    arquivo.write("Ola, qual o seu nome? e sua idade")
    
#responder
with open("cadastro.txt", "a") as arquivo:
    arquivo.write("\n meu nome é stefany e tenho 18 anos")
