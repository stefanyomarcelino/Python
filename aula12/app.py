# ARQUIVO ORGANIZADO

import pandas as pd

print("================================================")
print("        BEM - VINDO AO PORTAL DE ALUNOS")
print("================================================\n")
print("     Digite uma opção no menu")
print("         1 > criar")
print("         2 > Adicionar")
print("         3 > Apagar")
opcao = int(input("R: "))
   

if opcao == 1: #selecionar opçao 1
    print("Opção 1 SELECIONADA")
    
    
   #dados requesitados
    nome = str(input("Digite seu nome: ")) # str -> texto
    idade = int(input("Digite sua idade: ")) # int -> numero inteiro
    altura = float(input("Digite sua altura: "))



    dados = { #adicionar o dicionario com os dados agrupados
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
}

#armazenar dados no execel

    excel = pd.DataFrame(dados) # solicitar o armazenamento de dados  DATAFRAME

    excel.to_excel("aula12/Alunos.xlsx" , index=False) #criação do arquivo excel em formato DATAFRAME, ele guarda os dados

    print("Ação finalizada") #terminar processo




#segunda opção ADICIONAR NOVOS DADOS
elif opcao == 2:
    print('Opção 2 selecionada')
    nome = str(input("Digite seu nome: ")) # str -> texto
    idade = int(input("Digite sua idade: ")) # int -> numero inteiro
    altura = float(input("Digite sua altura: "))


    dados = { #adicionar o dicionario com os dados agrupados
        "nome": [nome],
        "idade": [idade],
        "altura": [altura]
    }
    

    leitura_excel = pd.read_excel("aula12\Alunos.xlsx")  #LEITURA DE EXECEL
    nova_linha = len(leitura_excel)

    leitura_excel.loc[nova_linha, "nome"] = dados["nome"] #ele le o excel 
    leitura_excel.loc[nova_linha, "idade"] = dados["idade"] #Ultilizar o LOC para criar um novo dedo ou ALTERAR um novo dado
    leitura_excel.loc[nova_linha, "altura"] = dados["altura"]
    
    
    
    leitura_excel.to_excel("aula12\Alunos.xlsx" , index=False) 
    print("Ação finalizada")
    
    



elif opcao == 3:  #Apagar a linha
    print("opeção 3 selecionada")
    linha_apagada = int(input("Digite um numero inteiro")) 
    leitura_excel = pd.read_excel("aula12\Alunos.xlsx") #LER EXCEL
     
    leitura_excel = leitura_excel.drop(linha_apagada)  #APAGAR EXCEL
    
    leitura_excel.to_excel("aula12\Alunos.xlsx" , index=False)  #SALVAR EXCEL
    
    print("Ação finalizada")

    
    