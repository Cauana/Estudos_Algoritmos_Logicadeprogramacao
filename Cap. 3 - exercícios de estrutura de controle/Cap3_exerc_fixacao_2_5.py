#Exercício Cap 3 -  exercício fixação 2.5

idade = int(input('Digite sua idade: '))

if idade >= 18:
    print('Você já pode tirar CNH e Votar')
elif 17>= idade >= 16:
    print('Você já pode votar, mas infelizmente ainda não pode tirar a sua CNH')
else: 
    print('Você não pode votar e nem tirar CNH')


