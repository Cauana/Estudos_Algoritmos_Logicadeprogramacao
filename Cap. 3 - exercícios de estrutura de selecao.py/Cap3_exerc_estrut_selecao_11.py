#classificação olímpica

maior = 0
menor = 1000000
for p in range(1,4):
    pais = str((input('Indique o país: ')))
    med_ouro = int(input('Qtdade medalha ouro: '))
    med_prata = int(input('Qtdade medalha prata: '))
    med_bronze = int(input('Qtdade medalha bronze: '))
    soma_med = (med_ouro*3)+(med_prata*2)+med_bronze
    if soma_med > maior:
        maior = soma_med
        paismaior = pais
    if soma_med == maior:
        print('Empate')
    if soma_med<menor:
        menor = soma_med
        paismenor = pais
    if soma_med<maior and soma_med>menor: 
        meio = pais 
        
print(f'1º lugar: {paismaior}')
print(f'2º lugar: {meio}')
print(f'3º lugar: {paismenor}')