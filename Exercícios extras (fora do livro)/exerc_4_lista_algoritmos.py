#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
#média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0 
import random

count = 0
listamedia = list()

for n in range(1,11):
    nota1 = random.randint(1,10)
    nota2 = random.randint(1,10)
    nota3 = random.randint(1,10)
    nota4 = random.randint(1,10)
    media = (nota1+nota2+nota3+nota4)/4
    print(nota1,nota2,nota3,nota4, media)
    listamedia.append(media)
print(listamedia)

for item in range(len(listamedia)):
    if listamedia[item]>=7:
        count += 1
print(f'o número de alunos acima da média é: {count}')