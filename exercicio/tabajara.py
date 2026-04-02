
# DESENVOLVIMENTO

# Crie um menu com as seguintes opções:
# 1 - Criar conta
# 2 - Acessar conta

# Regras para cada opção no menu
# 1 - Criar conta > Solicitar ao usuario para digitar as seguintes informações:
# - nome_cliente
# - cpf
# - tipo_conta

# O outros campos serão gerados de forma automatica
# - numero_conta = Será gerada de forma sequencial começando do 0 até 100
# - agencia = será gerado de forma sequencial começando do 400 até 700
# - extrato_bancario = valor inicial terá que começar em 0

# Ao finalizar mostrar para o usuário o nome_cliente, cpf, tipo_conta, numero_conta, agencia, extrato_bancario


# 2 - Acessar conta > É necessário que o usuário passe os seguites dados:
# - cpf
# - numero_conta
# > Precisa percorrer o excel e encontra o cliente com os mesmo dados de cpf e numero_conta caso encontre o cliente na base retornar uma mensagem: "Bem-vindo "nome_cliente" ao banco Tabajara" SENAO se o usuario não existir na base então retornamos uma mensagem "Usuário não encontrado, tentar novamente ou realizar o cadastro"
# """




#BANCO TABAJARA


import pandas as pd


#acessar conta
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("BEM VINDO AO BANCO TABAJARA 🏦")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("")

#Criar conta

print("Ja possui uma conta?:")

#opção 01
opcao = input("R:")

if opcao == "sim":
     print("digite o seu nome😀:")
     print("")#separar linha 
     nome = input("R:")
     

     #opcao 02   
elif opcao == "nao":
    print("Caso NÃO, FAÇA O SEU CADASTRO!!")
    ("Informe os seus dados aq ⬇️")   
    
    #dados selecionados
    nome = str(input("Digite seu nome: "))
    idade = int(input("Digite sua idade: "))
    email = (input("Digite o seu email: "))
    senha = (input("Digite sua senha: "))
    print("")#separar linha 
    
    #mostrar aos usuario
    print("NOME:",nome, "-" , "IDADE:",idade, "-", "EMAIL:",email, "-" "SENHA:",senha)
    
    print("Confirmar todos esse dados?")
    input()
    print("--------------------------")
    print ("CONTA CRIADA!!!🎉")
print()#separar linha 







    


# Regras para cada opção no menu
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("SEJA BEM VINDO", nome)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("")#separar linha 



#opçao para o usuario
print("Senhor(A)",nome, "Escolha uma das opções abaixo:")


print("1 - criar conta com dados bancarios  ")
print("--------------------------") 
print("2 - Acessar conta ")
print("--------------------------") 



#DADOS BANCARIOS

dados_bancarios = int(input("Digite um numero  (1 / 2 / 3):"))

if dados_bancarios == 1: #selecionar opçao 1
    print("Opção 1 SELECIONADA")
    
    print()#separar linha 
    
    print(" Digite os seus dados bancarios")
    nome_bancario = (input("Nome: "))
    cpf = float(input("CPF:"))
    tipo_conta = (input("CONTA:"))
    print() #separar linha
    
    
    #calculos
    numero_conta = 1 
    agencia = 400
    extrato_bancario = 0 
    
    
    dados = {#DICIONARIO GUARDANDO OS DADOS
    
    "nome_bancario": [nome_bancario],
    "cpf": [cpf],
    "tipo_conta": [tipo_conta],
    "numero_conta": [numero_conta],
    "agencia": [agencia],
    "extrato_bancario": [extrato_bancario]
    
}
    
     #chamar o excel   
    excel = pd.DataFrame(dados) 
    
    # excel.to_excel("exercicio/clientes.xlsx" , index=False)

    #CACULOS DOS EXTRATOS
    ler = pd.read_excel("exercicio/clientes.xlsx")
    numero_conta = len(ler) + 1
    agencia = 400 + len(ler)
    
    dados = {#DICIONARIO GUARDANDO OS DADOS
    
    "nome_bancario": [nome_bancario],
    "cpf": [cpf],
    "tipo_conta": [tipo_conta],
    "numero_conta": [numero_conta],
    "agencia": [agencia],
    "extrato_bancario": [extrato_bancario]
    
}
    
    nova_linha = len(ler)
    

    #RELER EXCEL
    ler.loc[nova_linha, "nome_bancario"]    = dados["nome_bancario"]
    ler.loc[nova_linha, "cpf"]             = dados["cpf"]
    ler.loc[nova_linha, "tipo_conta"]      = dados["tipo_conta"]
    ler.loc[nova_linha, "numero_conta"]    = dados["numero_conta"]
    ler.loc[nova_linha, "agencia"]         = dados["agencia"]
    ler.loc[nova_linha, "extrato_bancario"]= dados["extrato_bancario"]


    ler.to_excel("exercicio/clientes.xlsx" , index=False)
    print("Arquivo Excel gerado com sucesso!")
    print()

  
  
    #mostrar ao cliente

    print("Todos os dados informados")
    print(nome_bancario, "--", cpf, "--", tipo_conta)


    print()#separar linha
    print(numero_conta)

    print()#separar linha
    print(agencia)

    print()#separar linha
    print(extrato_bancario)
        




#OPÇÃO 2

elif dados_bancarios == 2:
    print("Opção 2 SELECIONADA")
    
    print()
    print("Digite os seus dados bancários")
    
    cpf = str(input("CPF: "))
    numero_conta = int(input("Numero conta: "))
    
    ler = pd.read_excel("exercicio/clientes.xlsx") 
    
    cliente_encontrado = False

    for index, linha in ler.iterrows():
        
        if pd.isna(linha["cpf"]):  # ignora linha com CPF vazio
            continue
            
        cpf_excel = str(int(float(linha["cpf"])))
        conta_excel = int(linha["numero_conta"])

        if cpf_excel == cpf and conta_excel == numero_conta:
            cliente_encontrado = True
            nome_cliente = linha["nome_bancario"]
            print(f'Bem-vindo {nome_cliente} ao banco Tabajara!')
            break

    if not cliente_encontrado:
        print("Usuário não encontrado, tentar novamente ou realizar o cadastro")


    print("") #separar linha

    dados_bancarios = print("Voce escolheu: Saque, Deposito, Saldo ")

    print("") #separar linha

    print("O que deseja fazer?:")

    print("")#separar linha

    print("1 - Saque")
    print("2 -  Deposito")
    print("3 -   Saldo")

    print("") #separar linha




#==============OPÇÃO SAQUE ============
    opcao = int(input("R: "))

    if opcao == 1:
        # ── SAQUE 
        print("") #pular linha
        valor_solicitado = int(input("  Digite o valor para saque: R$ ")) # Digitar valor
        
        taxa_saque = ()
        
        taxa_saque = valor_solicitado * taxa_saque
        saldo = extrato_bancario - valor_solicitado - taxa_saque
        


        print("================================================")
        print("      Saque realizado com sucesso!💸")
        print(f"      Saque: R$ {valor_solicitado}")
        print(f"      Valor em conta: R$ {saldo}")
        print(f"      Taxa para saque ({tipo_conta}): {taxa_saque * 100}%")
        print(f"      Valor de desconto saque: R$ {taxa_saque}")
        print("================================================\n")





#  =========== OPÇÃO DEPOSITO ==============
    elif opcao == 2: 
        
        ler = pd.read_excel("exercicio/clientes.xlsx")
        valor_deposito = ()
        
        
        print(f"  Saldo atual em conta: R$ {extrato_bancario}")
        print("")
        
        
        valor_deposito = int(input("Digite o valor para deposito:"))
        print("")
        extrato_bancario = extrato_bancario + valor_deposito
        
        
        print("================================================")
        print(f"      Valor depositado: R$ {valor_deposito}")
        print(f"      Saldo em conta: R$ {extrato_bancario}")
        print("================================================\n")

        ler.to_excel("exercicio/clientes.xlsx" , index=False)
    
        
    
    
    
    
    
    
    # ============ OPÇÃO SALDO ============
        
        
    elif opcao == 3:
        
        print("Sua conta e seu saldo: ")
        
        print("")
        print("================================================")
        print(f"   Tipo conta: {tipo_conta}")
        print(f"   Saldo em conta: R$ {extrato_bancario}")
        print("================================================\n")
        






    
    
    

    
    
    
    
    


    








    

