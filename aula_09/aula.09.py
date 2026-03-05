# criar uma função

def saudação():
    print("Ola, seja bem-vindo")
    
    #precisa chamar A FUNÇÃO CRIADA, não adianta so escrever

saudação()



# Adicionar um nome do cliente


nome = "Beltrano" #Colocar o nome da pessoa PARA PARECER NA SUA FUNÇÃO

def ola_pessoa():
    print("Ola, seja bem-vindo", nome)
    
(ola_pessoa(nome)) # Chamar uma função 


# CALCULA recebe dois valors e faz a soma, retorna o resultado
salario_funcionario = 3000
beneficio = 400

def salario(valor1, valor2):
    return valor1  + valor2 

print(salario(salario_funcionario, beneficio))
    
    
    
    
# SOMA DOIS VALORES SE(IF) A IDADE DO USUARIO FOR IGUAL OU MAIOR A 18
#SENÃO MOSTRAR MENSAGEM "idade invalida"

nome_usuario = int(input("Digite sua idade")) #ESCOLHA DO USUARIO

if(nome_usuario >= 18): 
    var1 = int(input("Digite o primeiro valor"))
    var2 = int(input("Digite o segundo valor"))
    
    resultado = (var1 + var2)
    
    print(resultado)
    
else:
    print("Sua idade é menor que 18")


#MUITO IMPORTANTE LEMBRAR E ESTUDAR 


#Nativas do python São super simples 📟


 # Retorna a quantidade de itens e funciona com strings
lista = [1,3,4,56,10] #conta a quantidade de palavras
palavra = "ano"
print(len(lista)) #função da LEN = Retornar a quatidade de informações em uma variavel

print(len(palavra))

frase = "sua mae te ama muito em slk"
print(len(frase)) #conta a quatidade de palavras


#Função SUM
print(sum(lista)) #SOMA TODA A MINHA LISTA NUMERICA


#MAX () 
print("Maior", max(lista)) #RETORNA O MAIOR VALOR

# MIN ()
print("Menor", min(lista)) #Retorna o MENOR VALOR


# SORTED 

print(sorted(lista)) #ORDENA TODOS OS NUMEROS PRA VC, NUMEROS DA SUA LISTA

# TYPE 
tipo = 10.00
print(type(tipo)) # Retorna o TIPO da sua lista


# Conversão de tipos
print(float(tipo)) #TRADUZ NUMEROS PARA TEXTO

print(int(tipo)) #TIRA FONTOS FLUTUANTES (10.0 TIRA O .0)



