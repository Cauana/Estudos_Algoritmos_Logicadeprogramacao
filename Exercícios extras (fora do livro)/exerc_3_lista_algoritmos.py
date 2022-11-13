#. Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os
#números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. 

lista = [46, 100, 36, 15, 68, 84, 64, 46, 38, 62, 26, 45, 33, 50, 45, 43, 17, 50, 11, 40]
listapar = []
listaimpar = list()

for item in range(len(lista)):
    if lista[item] % 2 == 0:
        listapar.append(lista[item])
    else:
        listaimpar.append(lista[item])

print(lista)
print(listapar)
print(listaimpar)