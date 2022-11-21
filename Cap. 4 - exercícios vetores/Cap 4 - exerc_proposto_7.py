#União de elementos em duas listas
#Dúvida
import random
lista1 = []
lista2 = []


for num in range(1,5):
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    lista1.append(numero1)
    lista2.append(numero2)
    
print(lista1)
print(lista2)

listauniao = []

for n in range(len(lista1)):
    if lista1[n] in listauniao:
        continue
    else:
        listauniao.append(lista1[n])

for i in range(len(lista2)):
    if lista2[i] in listauniao:
        continue
    else:
        listauniao.append(lista2[i])
print(listauniao)
