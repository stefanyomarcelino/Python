#Dicionario em python tipo um biblioteca

aluno = {    #criando valores chumbados
    #"chave" : valor
    "nome" : "Pedro",
    "idade" : 20,
    "nota" : 8,
  "curso" : "Tecnico TI",
  
  
  #ultilizando uma Array para agrupar informaçoes 
  "Array": [30, True, "texto"],
  
  
  
  #Dicionario dentro de um dicionario
   "endereco" : {
       "rua": 3,
       "cidade" : "SP",
       "estado": "SP",
   }
  }




#Acessando valores do dicionario, mostrando para o cliente 
print(aluno["nome"])
print(aluno["idade"]) #sempree chamar o DICIONARIO (Chamar o vendedor)
print(aluno["nota"])
print(aluno["curso"])



#Acessar um UNICO dado do endereço quando fizer um DICIONARIO DENTRO DE UM DICIONARIO
print(aluno["endereco"] ["cidade"])





#Alteração de dados (o aluno fez aniversario!!)
aluno["idade"] = 20

print(aluno["idade"])




#Alterar dados dentro de um array que esta dentro de um dicionario
aluno["Array"][2] = 9 #chamar a ARRAY para alterar o valor
print(aluno["Array"][2])




#Alterar dados do DICIONARIO endereco que esta dentro dfo dicionario ALUNO
aluno["endereco"]["cidade"] = "São paulo"  #sempre que precisar adicionar uma chave dentro de um dicionario USAREMOS COLCHETES [caso quero um campo MAIS ESPECIFICO, DNV COLOCO COLCHETES []]
print(aluno["endereco"]["cidade"])





#ADICIONAR NOVOS DADOS/CHAVES
aluno["periodo"] = "noturno" #adicionar um novo codigo pro dicionario que ja existe sem ser chumbado, tipo um novo rotulo
print(aluno)



#REMOVER DADOS, criamos agora vamos removelos (usar DEL sempre no começo da palvra)
del aluno["idade"], aluno["nome"] #adicinar DEL no começo/ para deletar mais de um so colocar , aluno["nome"]
print(aluno)






#PERCORRER DICIONARIOS
for chave in aluno:  #VC descreve todos os seus DICIONARIOS  ex: ENDERECO, ALUNO, ARRAY...
    print(chave)



#usando um laço de repeticao para retornar os valores
for valor in aluno.values(): #values so quer RETORNAR OS VALORES DENTRO DO DICIONARIO (apenas os valores)
    print(valor)




#PERCORRER DICIONARIO E RETORNAR A CHAVE E VOLTAR
for chave, valor in aluno.items(): #deixa o terminal mais "limpo" sem aqueles monte de traço e virgula. Ele permite deixar mais limpo e organizado
    print(chave, ":", valor)



