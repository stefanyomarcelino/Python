# lista vazia 
Compras = []

#digite 3 itens
for i in range(3):
    item = input("Digite um item:")
    Compras.append(item)
    
    print("sua lista de compras:", Compras)
    
    for valor in Compras:
        print("-", valor)




