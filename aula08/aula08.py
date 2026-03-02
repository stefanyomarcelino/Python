#Listas []--> Para acessar dados usamos: POSIÇÃO DA LISTA
#Dicionarios {} --> para acessar dados usamos: NOME/CHAVE

notas = [10, 8, 4, True , 9, 7, "Notas do Ruan"]   #[para indicar ao python que é uma LISTA]  
#segue as mesmas prosiçoes das STRINGS, cada dados tem uma posição



 #APPEND ele adiciona um item ao final da lista
notas.append("reprovado")
print(notas)



#INSERT ele insere um item em posição especifica, empura para frente, vc pode adicionar a posição especifica ou um Boolean
notas.insert(0, False)
print(notas)


#EXTEND ele adiciona varios itens juntos 

nova_lista =  ["listas dos valores", 24.7]
nova_lista.extend(notas)
print(nova_lista)

#REMOVE NUMEROS/TEXTOS DOS CODIGOS
notas.remove(10)
print(notas)
notas.remove(True)
print(notas)



#Remover texto
notas.remove("Notas do Ruan")
print(notas)
#notas.remove ("Ruan") #metodo remove é case Sens




#POP ele REMOVE pelo indice, vc pode remover numeros, nomes, pelo POP 
nomes_nume = [390, "stefany", 45, "Anna", 45, "Israel", 390]
nomes_nume.pop(2)
print(nomes_nume)



#CLEAR ele LIMPA sua lista TODA/ ele limpa o terminal tmb
print(nomes_nume.clear())




#INDEX ele RETORNA a posição do item
#print(nomes_nume.index("stefany")) 
print(nomes_nume)



#COUNT ele CONTA OCORRENCIAS
print(nomes_nume.count(45))



#SORT ele ordena numeros e nomes
numeros = [34, 45, 59, 67, 26, 80, 101, 50, 21, 5]
numeros.sort()
print(numeros)



#ordenar nomes
nome = ["stefany", "israel", "vanessa", "anna", "isabela"]
nome.sort()
print(nome)



#REVERSE ele inverte a ordem da  lista
numeros.reverse()
print(numeros)

nome.reverse()
print(nome)

