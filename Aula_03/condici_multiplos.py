
#IF ELSE   (ultilizado para mais de um resposta) MAIS DINAMICO
idade = 17

if idade > 18:
    print("Maior de idade") #identação sempre precisa ter
else: #mais de uma resposta/ sempre o resto
    print("Menor de idade, por favro solicitar um responsavel")
    
    
    
    #Mais flexivel
valida_idade = int(input("digite sua idade"))
if valida_idade <18: 
    print("Voce é menor de idade")
else:
    print("voce é maior de idade")    