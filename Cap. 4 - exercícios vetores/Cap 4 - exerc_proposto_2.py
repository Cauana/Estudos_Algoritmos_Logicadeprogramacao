#Inverter a posição dos valores de um vetor
import random

lista = []
lista2 = []
num = 29
for c in range(1,31):
    r = random.randint(1,10)
    lista.append(r)

while num > -1:
    lista2.append(lista[num])
    num -= 1
print(lista)

#lista invertida
print(lista2)

#Também é possível inverter dessa forma
print(lista2[::-1])