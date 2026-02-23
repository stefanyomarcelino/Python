
     #ESSE EU QUASE ME MATEI   
        
numero_tabuada = input("Digite um número: ")

if numero_tabuada.isdigit() > 0:
    numero_tabuada = int(numero_tabuada)
    print(f"Tabuada do numero {numero_tabuada}: ")
    for numero in range(1, 11):
        resultado = numero_tabuada * numero
        print(f"{numero_tabuada} x {numero} = {resultado}")
    else:
        print("Número iválido, digite outro entre 1 e 10!")

 

    
    