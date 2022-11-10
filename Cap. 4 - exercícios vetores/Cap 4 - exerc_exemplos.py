#Soma de vetores

listaA = [1,2,3,4,5,6]
listaB = [7,8,9,10,11,12]

listaresult = listaA + listaB
print(listaresult)

# coloca 1 para índice par e 0 para ímpar
lista = list(range(0,100))
for item in lista:
    if item%2==0:
        lista[item] = 1
    else:
        lista[item] = 0
print(lista)
        