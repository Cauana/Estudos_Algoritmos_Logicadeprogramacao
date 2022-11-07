#Exercício Cap 3 -  exercício fixação 2.4

altura = float(input('Digite sua altura: '))
sexo = str(input('Digite seu sexo: (M / F)'))
sexo = sexo[0]
sexo.upper()
print(sexo)
if sexo in 'Mm':
    pesoideal = (72.7 + altura) - 58
    print(f'Seu peso ideal é {pesoideal}kg')
if sexo in 'Ff':
    pesoideal = (62.1 + altura) - 44.7
    print(f'Seu peso ideal é {pesoideal}kg')

