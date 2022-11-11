#50 notas e calcule quantas acima de 10% da média
# e quantas abaixo de 10%

import random
soma = 0
countmenor = 0
countmaior = 0
lista = []
lista2 = []

for c in range(1,51):
    r = random.randint(1,10)
    lista.append(r)
print(lista)
    
for item in range(len(lista)):
    soma = soma + lista[item]
med = soma / (len(lista))
print(f'A média das 50 notas é {med}')

for item in range(len(lista)):
    if lista[item]>(med*1.10):
        countmaior += 1
    if lista[item]<(med*0.9):
        countmenor += 1
        
print(f'Quantidade de notas 10% acima da média {countmaior}')
print(f'Quantidade de notas 10% abaixo da média {countmenor}')
