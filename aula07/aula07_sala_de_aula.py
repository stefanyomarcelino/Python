#criar um dicionario para o aluno digitar


#dados do aluno
aluno_dados = "nome", "idade", "cidade"


#Coleta de dados/ o aluno digita
nome = (input("Digite seu nome"))
idade = (input("Digite sua idade"))
cidade = (input("Digite sua cidade"))


#guardar essas informaçoes

aluno_dados = {
    "nome": nome,
    "idade": idade,
    "cidade" : cidade,
    
}


#mostrar informaçoes
print(aluno_dados)


#Exercicio 2
#Criar um dicionario com dados digitados pelo usuario



#dados do aluno
dados_digitados = "nota1" "nota2" "nota3" "nota4" "nota5"



#Coletar dados do usuario
nota1 = int(input("Digite a nota"))
nota2 = int(input("Digite a nota"))
nota3 = int(input("Digite a nota"))
nota4 = int(input("Digite a nota"))
nota5 = int(input("Digite a nota"))


#calculo da media 

media = (nota1 + nota2 +  nota3 +  nota4 + nota5) / 5



print(media)
