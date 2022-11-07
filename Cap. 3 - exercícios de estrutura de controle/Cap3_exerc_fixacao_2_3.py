#Exercício Cap 3 -  exercício fixação 2.3

A = int(input('Digite o valor de A: '))
B = int(input('Digite o valor de B: '))
C = int(input('Digite o valor de C: '))

delta = (B**2) - 4*A*C

if delta>0:
    x1 = (-B + (delta**0.5)) / (2*A)
    x2 = (-B - (delta**0.5)) / (2*A)
    print(f'As raízes são: {x1} e {x2}')
if delta == 0:
    x = (-B + delta**(1/2)) / 2*A
    print(f'A raíz é {x} e o delta dessa equação é {delta}')
if delta < 0:
    print('Não existem raízes válidas')