#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos 
#quadrados dos elementos do vetor.
import random
soma = 0
lista = []

for n in range(1,4):
    n1 = random.randint(1,100)
    lista.append(n1)
print(lista)

for i in range(len(lista)):
    quadrado = lista[i]**2
    soma += quadrado
    
print(f'A soma dos quadrados dos números da lista é {soma}')
