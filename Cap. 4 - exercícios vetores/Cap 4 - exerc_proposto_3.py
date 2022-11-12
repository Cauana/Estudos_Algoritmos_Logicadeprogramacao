#maior sequência dentro de uma lista de números

import random

lista = []
countseq=1
countseqatual = 0
for i in range(1,31):
    n= random.randint(1,5)
    lista.append(n)
  
print(lista)  
for c in range(0,8):
        if lista[c]<lista[c+1]:
            d = lista[c+1]-1
            if lista[c] == d:
                countseq += 1
                if countseq >= countseqatual:
                    countseqatual = countseq
   

print(f'Maior sequência: {countseqatual}')

    