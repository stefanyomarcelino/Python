#Crie uma lista com 4 nomes
    
print("Observe os nomes")
Nomes = ["Iza", "Megan", "Bruna", "Ster"]
print(Nomes)
 
 #Remova um dos nomes
Nome_Remover = input("Remova um dos nomes: ")
 
 
 #nome removido
if Nome_Remover in Nomes:
    Nomes.remove(Nome_Remover)
    print("Nome removido")
else:
    print("Nome não encontrado")
 
print("Lista final:", Nomes)
    


