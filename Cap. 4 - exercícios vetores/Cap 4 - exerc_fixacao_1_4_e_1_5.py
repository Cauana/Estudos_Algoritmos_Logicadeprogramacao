#ordenação de vetores

#ordem crescente

lista = [5,2,10,1,4]

for item in range(len(lista)):
    for j in range (len(lista)):
        if lista[item] <= lista[j]:
            temp = lista[item]
            lista[item] = lista[j]
            lista[j] = temp
print(lista)

#ordem decrescente

lista = [5,2,10,1,4]

for item in range(len(lista)):
    for j in range (len(lista)):
        if lista[item] >= lista[j]:
            temp = lista[item]
            lista[item] = lista[j]
            lista[j] = temp
print(lista)

