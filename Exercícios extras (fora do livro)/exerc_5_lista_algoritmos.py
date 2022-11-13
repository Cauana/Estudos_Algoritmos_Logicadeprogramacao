#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e
#os números. 
import random

soma = 0
mult = 1
lista = list()

for n in range(1,6):
    num = random.randint(1,10)
    lista.append(num)
print(lista)

for item in range(len(lista)):
    soma += lista[item]
    mult *= lista[item]
print(f'A Multiplicação de todos os n da lista é: {mult} e a soma é {soma}')