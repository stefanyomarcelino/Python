#Bilbiotecas codigos pronto para resolver problemas 

#Importação de biblioteca 
  #IMPORT RANDOM (para trazer uma biblioteca para o seu arquivo)
  
  
import random #RANDINT SO GERA NUMEROS ALEATORIO 🏳️
import math # MATH PARA CONTAS
import datetime

numero_alt = random.randint(1000, 2000 )  #Responsavel por dar um numero aleatorio 
print(numero_alt)


#sorteio individual aleatorio

alunos = ["Ster", "Ana", "Israel", "Wellington", "Maria", "Camy", "Lucas", "Guilherme"]  #variavel com nomes

# CHOICHE PARA ESCOLHER 
sorteado = random.choice(alunos)  # VARIAVEL + BIBLIO(VARIAVEL)
sorteado2 = random.choice(alunos)

print("Dupla escolhida para o projeto", sorteado, "-" , sorteado2) #PRINT + VARIAVEL para mostrar ao usuario



# BIBLIOTECA MATH ➕🟰➗➖

Numero = 35

raiz = math.sqrt (Numero)  # VARIAVEL + MATH.SQRT
print(raiz)


#ELEVAR NUMERO (POTENCIA) 🛗 (funçao : POW💣)

print(math.pow(2,2)) #NUMERO ELEVADO
print(math.pow(4,6)) #NUMERO ELEVADO 
print(math.pow(8,3)) #NUMERO ELEVADO


# DATETIME (dias, datas, horarios) 🕰️

agora = datetime.datetime.now() #ACESSAR O DATETIME DENTRO DA DATETIME( um é a chamada da biblio e a outra é DENTRO da biblio, e colocar o NOW para ser a data de AGORA)
print(agora.hour) #.hour para retornar a HORA DENTRO DO PRINT
print(agora.month)
print(agora.minute)
print(agora.second)
print(agora.microsecond)
print(agora.day)



#atividade para exercicitar o IMPORT


#solicitar um numero de 1 a 5 
#gerar um numero aleatorio usando a biblio random.
#verificar se o usuario digitou o mesmo valor que o resultado da biblio

import random
notas = []
valor = 1
numero_usuario = int(input("Digite um numero de 1 a 5"))

for notas in range(1):
     numero_usuario = int(input("Digite um numero de 1 a 5"))    
    
numero_bet = random.randint(1, 5)
if numero_usuario == numero_bet: #IF SE ELE FOR IGUAL AO NUMERO 
    print("PARABENS GANHOU UMA PORRADA DE COISA")
else:
    print("PARABENS NAO GANHOU PORRA NENHUMA, TENTA DNV") 
    
    


         
         
               
    
    
     


