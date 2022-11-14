'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em 
uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas 
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 
2 – Fevereiro, . . . ). '''
import random

count = 0
soma = 0
listatemp = list()

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
            if p == 0:
                print(f'O mês de janeiro teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 1:
                print(f'O mês de fevereiro teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 2:
                print(f'O mês de março teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')          
            elif p == 3:
                print(f'O mês de abril teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 4:
                print(f'O mês de maio teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 5:
                print(f'O mês de junho teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 6:
                print(f'O mês de julho teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 7:
                print(f'O mês de agosto teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 8:
                print(f'O mês de setembro teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 9:
                print(f'O mês de outubro teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 10:
                print(f'O mês de novembro teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')
            elif p == 11:
                print(f'O mês de dezembro teve temperatura acima da média anual. Temperatura de {listatemp[p]}ºC')