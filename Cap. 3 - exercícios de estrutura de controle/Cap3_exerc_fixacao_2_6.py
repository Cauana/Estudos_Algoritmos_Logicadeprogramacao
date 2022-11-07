#Exercício Cap 3 -  exercício fixação 2.6

codigo = int(input('Digite o código do produto: '))

if codigo >= 16:
    print('Inválido')
else:
    if codigo ==1:
        print('Alimento não perecível')
    elif 1 < codigo < 5:
        print('Alimento perecível')
    elif 5 <= codigo <= 6:
        print('Vestuário')
    elif codigo == 7:
        print('Higiene pessoal')
    elif 8 <= codigo <= 15:
        print('Limpeza e utensílios domésticos')