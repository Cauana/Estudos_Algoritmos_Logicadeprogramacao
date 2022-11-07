#Exercício Cap 3 -  3.7

valorproduto = int(input('Valor do produto: '))
codigo_origem = int(input('Código do produto: '))

if codigo_origem == 1:
    print('Sul')
if codigo_origem == 2:
    print('Norte')
if codigo_origem == 3:
    print('Leste')
if codigo_origem == 4:
    print('Oeste')
if codigo_origem == 5 or codigo_origem ==6:
    print('Nordeste')
if 6<codigo_origem<10:
    print('Sudeste')
if 9<codigo_origem<21:
    print('Centro-Oeste')
if 25<=codigo_origem<31:
    print('Nordeste')
if codigo_origem>30:
    print('Produto importado')
    

#Fixação 2 
#2.1
'''
a) C1 c6
b) C3 C4 c5 c6
c) C2 c5 c6
ff ni
fff




'''