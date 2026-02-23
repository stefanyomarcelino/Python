#IF - ELIF - ELSE (MAIS OPEÇOES )

nota = int(input("Digite a nota do aluno"))
nome_aluno = input("digite o nome do aluno")

if nota >= 9:
    print(f"O aluno {nome_aluno} esta aprovado com a nota {nota}")
elif nota >= 7 and nota <= 8:
    print(f"O aluno {nome_aluno} esta aprovado por conselho com a nota {nota}")
else:
    print(f"O aluno {nome_aluno} esta reprovado com a nota {nota}")
    