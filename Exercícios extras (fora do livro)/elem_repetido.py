#Faça um programa que percorra duas listas e gere uma terceira sem
#elementos repetidos.
import random
lista1 = []
lista2 = []
listaresultado = []

for n in range(10):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    lista1.append(n1)
    lista2.append(n2)
    
print(lista1)
print(lista2)

for n in range(len(lista1)):
    if lista1[n] in listaresultado:
        continue
    else:
        listaresultado.append(lista1[n])

for n in range(len(lista2)):
    if lista2[n] in listaresultado:
        continue
    else:
        listaresultado.append(lista2[n])
    
print('A lista resultante é:', end=' ')
print(listaresultado)

#Organizando a lista em ordem crescente
for i in range(len(listaresultado)):
    for j in range(len(listaresultado)):
        if listaresultado[i]<=listaresultado[j]:
            temp = listaresultado[i]
            listaresultado[i] = listaresultado[j]
            listaresultado[j] = temp
            
print('A lista resultante em ordem crescente é:', end=' ')
print(listaresultado)