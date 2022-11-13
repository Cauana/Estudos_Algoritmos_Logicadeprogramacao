#Leia um vetor de 10 elementos e calcule o maior e o menor valor.
maior = 0
menor = 9999999999999
lista = [15,23,65,21,9,47,37,60,80,62]

for item in range(len(lista)):
    if lista[item] > maior:
        maior = lista[item]
    elif lista[item]<menor:
        menor = lista[item]        

print(f'O menor item da lista é {menor} e o maior item da lista é {maior}')