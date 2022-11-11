#Gerar um segundo vetor que as posições pares são o dobro do vetor original
#e que as posições ímpares são o triplo do vetor original
#Lembrando que os índices começam em 0
import random

lista = []
lista2 = []

for c in range(1,31):
    r = random.randint(1,10)
    lista.append(r)

for item in range(len(lista)):
    if item%2 != 0:
        temp = lista[item]*3
        lista2.append(temp)
    elif item%2 == 0:
        temp = lista[item]*2
        lista2.append(temp)
        
print(lista)

print(lista2)