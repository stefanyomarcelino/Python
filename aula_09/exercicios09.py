#Criar um função que receba 5 notas 3

#Criação de uma função 

lista_notas = []
valor = 1
 
 
def recebe_nota():
   
    for valor in range(5):  #ranger fazendo a função de looping repetindo as 5 notas
        nota = int(input("Digite um valor: "))
        lista_notas.append(nota) #append para ADICIONAR a lista
 
 
    #return lista_notas
 
    valor = (sum(lista_notas) / len(lista_notas)) #SUM para somar as notas dentro da list, e dividimos / pela quantidade de valores na lista (LEN)
    print(valor)
    print(valor)
    return valor
   
   
 
#recebe_nota(1)
 
def resultado_aluno(): #Definir a função para ver se o aluno esta aprovado
   
    valor = recebe_nota()
    if valor >= 5:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
 
 
resultado_aluno()



#prof o israel me ajudou pq eu nao tava conseguindo, salvei o codigo dele pra estudar