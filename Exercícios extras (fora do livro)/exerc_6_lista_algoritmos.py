#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no
#seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida. 
import random

item = 4
listaidade = list()
listaaltura = list()
listaidadeinversa = []
listaalturainversa = []

for n in range(1,6):
    idade = random.randint(10,99)
    altura = random.randint(130,200)
    listaidade.append(idade)
    listaaltura.append(altura)
print(listaidade)
print(listaaltura)

while item >-1:
    listaidadeinversa.append(listaidade[item])
    listaalturainversa.append(listaaltura[item])
    item -= 1

print(listaalturainversa)
print(listaidadeinversa)