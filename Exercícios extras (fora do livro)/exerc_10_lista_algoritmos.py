'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em 
uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas 
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 
2 – Fevereiro, . . . ). '''
import random

count = 0
soma = 0
listatemp = list()
mes = ['janeiro','fevereiro', 'março', 'abril', 'maio', 'junho', 'julho','agosto','setembro','outubro','novembro','dezembro']
for n in range(1,13):
    temp = random.randint(1,35)
    listatemp.append(temp)
    
print(listatemp)

for i in range(len(listatemp)):
    soma += listatemp[i]
    media = soma/len(listatemp)
print(soma)
print(media)

for p in range(len(listatemp)):
    if listatemp[p]>media:
            print(f'O mês de {mes[p]} teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')