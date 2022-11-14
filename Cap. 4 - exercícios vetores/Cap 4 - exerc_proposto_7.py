#União de elementos em duas listas
#Dúvida
import random
lista1 = []
lista2 = []


for num in range(1,21):
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    lista1.append(numero1)
    lista2.append(numero2)
    
print(lista1)
print(lista2)

listauniao = lista1+lista2
print(listauniao)


for i in range(1,38):
    for n in range(1,38):
        if listauniao[i] == listauniao[n]:
            del(listauniao[i])
print(listauniao)
