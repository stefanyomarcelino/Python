#Se o usuario for menor de idade, então ele precisa ter autorização
#Se o usuario for maior de idade, ele então precisa ter a altura minima

idade_cliente = int(input("digite a idade do cliente")) #Mais dinamico esse modelo com INT e INPUT
altura_cliente = float(input("Digite a sua altura"))

if idade_cliente < 18:
    print("Voce é maior de idade, e tem altura minima para o brinquedo")
else:
    if altura_cliente >= 1.50:
        print("O cliente tem a altura estimada para o brinquedo")
    else:
        print(" mesmo vocé sendo maior de idade, vocé não tem altura sufuciente para esse brinquedo, minimo 1.50")
    #print("o cliente é maior de idade pode subir no brinquedo")
    