#Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos 
#alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
import random

count = 0
soma = 0
listaidade = list()
listaaltura = list()
lista = []

for n in range(1,11):
    n1 = random.randint(1,50)
    n2 = random.randint(100,200)
    listaidade.append(n1)
    listaaltura.append(n2)
print(listaidade)
print(listaaltura)

for i in range(len(listaaltura)):
    soma += listaaltura[i]
    media = soma/len(listaaltura)
print(soma)
print(media)

for p in range(len(listaaltura)):
    if listaidade[p]>13:
        if listaaltura[p]<media:
            count += 1
            print(f'Menor que a média de altura: altura {listaaltura[p]} e idade {listaidade[p]}')
        
print(f'{count} alunos estão abaixo da média de idade e tem idade maior que 13 anos')