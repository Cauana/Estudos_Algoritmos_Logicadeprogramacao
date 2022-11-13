#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20
#elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros
#vetores. 
import random

item = 4
lista1 = list()
lista2 = list()
lista = []

for n in range(1,11):
    n1 = random.randint(1,100)
    n2 = random.randint(1,100)
    lista1.append(n1)
    lista2.append(n2)
print(lista1)
print(lista2)

for n in range(0,10):
    lista.append(lista1[n])
    lista.append(lista2[n])
print(lista)