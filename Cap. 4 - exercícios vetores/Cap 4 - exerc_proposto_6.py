#Intersecção de elementos em duas listas
import random
lista1 = []
lista2 = []
listainterseccao = []


for num in range(1,21):
    numero1 = random.randint(1,100)
    numero2 = random.randint(1,100)
    lista1.append(numero1)
    lista2.append(numero2)
    
print(lista1)
print(lista2)

for i in range(len(lista1)):
    for n in range(len(lista2)):
        if lista1[i] == lista2[n]:
            n = lista1[i]
            listainterseccao.append(n)
print(listainterseccao)