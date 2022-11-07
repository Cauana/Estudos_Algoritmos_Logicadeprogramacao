#Exercício Cap 3 -  exercício fixação 2.9
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)

if imc < 18.6: 
    print('Abaixo do peso')
if imc > 30: 
    print('Obesidade')
if 18.5 <= imc <= 25: 
    print('Peso Normal')
if 25 <= imc <= 30: 
    print('Acima do peso')
print(f'Seu IMC é: {imc:.2f}')