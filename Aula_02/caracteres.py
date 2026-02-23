
 #Caracters
texto1 = "SENAC"

print(texto1[0]) #Contar 
print(texto1[1])
print(texto1[2]) # -1 para ir ate a ULTIMA letra 
print(texto1[3])
print(texto1[4])



# Função (LEN)

texto02 = "ola"
print(len(texto02)) #Verificar a quantidade de caracteres

# Texto maior
texto03 = "Desafios: Considerado um instrumento difícil por não ter trastes (notas marcadas), exigindo audição treinada, postura não natural e coordenação motora para o arco. Embora clássico, é usado em folk, jazz e música pop."
print(len(texto03))
  
    
# Texto em outra lingua
texto04 = "Lorem Ipsum，也称乱数假文或者哑元文本， 是印刷及排版领域所常用的虚拟文字。由于曾经一台匿名的打印机刻意打乱了一盒印刷字体从而造出一本字体样品书，Lorem Ipsum从西元15世纪起就被作为此领域的标准文本使用。它不仅延续了五个世纪，还通过了电子排版的挑战，其雏形却依然保存至今。在1960年代，”Leatraset”公司发布了印刷着Lorem Ipsum段落的纸张，从而广泛普及了它的使用。最近，计算机桌面出版软件”Aldus PageMaker”也通过同样的方式使Lorem Ipsum落入大众的视野。"
print(len(texto04))





# Maiusculas e Minusculas

text05 = "eu sou linda"
print(text05.upper()) #posso padronizar para nao quebrar o meu codigo

text06 = "EU SOU GATONA"
print(text06.lower())

print(text05.capitalize()) #deixa em maiusculo a primeira letra

print(text05.title())




# Substring


text07 = "python"
print(text07[0:3]) #retorne ATE a posição solicitada ignorando as diantes 3 = PYT (H é ignorado)
print(text07[0:5])



#REPLACE

text08 = "eu odeio python"

novo_texto = text08.replace(" odeio python", " gosto de java") #ele troca as palavras
print(novo_texto)




# ESQUERDA ESPAÇO EM BRANCO

text09 = "   oi mundao   "
print(text09.strip() + "string") # remove direita e esquerda
print(text09.lstrip() + "string") # remove esquera
print(text09.rstrip() + "string") #remove direta


# METODO (IN)

text10 = "adoro bolo de red velvet, mas nao tenho dinheiro pra comprar"
print("red velvet" in text10)  #procurar a palavra e retornar como TRUE  ou FALSE
#case sensitive = sensivel a letras maiusculas e minusculas 

print(text10.find("dinheiro"))
print(text10[40]) #posição


print(text10.count("e")) #todas as letras E que tem na frase


text11 = "red velvet"  #True ou False para as iniciais das frase
print(text11.startswith("red"))
print(text11.endswith("et"))