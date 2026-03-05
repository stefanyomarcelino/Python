#  Abrindo arquivos no python

open("nota.txt", "w") #nome do arquivo e escolha do arquivo, W, R, A
#após fazer isso, o arquivo vai ser criado no EXPLORADOR 
#with é o "SALVAMENTO AUTOMATICO DO ARQUIVO" enquanto o WRITE vc escreve, o OPEN vc abre o arquivo, o WITH é o salvamento


#Abrir um arquivo e digitar informaçoes (W)
with open("aula10/nota.txt", "w") as nota_aluno:
     nota_aluno.write("ola galera, bem vindos, aula de sofrimento") #para executar um arquivo 
     
     #Leitura de arquivos (R)
     with open("aula10/nota.txt", "r") as leitura_arquivo:
         reecebe_texto = leitura_arquivo. read()
     print(reecebe_texto)
     
     
     #Adicionar um texto ao final do arquivo (A)
     with open("aula10/nota.txt", "a") as adiciona_novo_texto:
         adiciona_novo_texto.write("\n aq tem uma nova linha ")