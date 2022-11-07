#Calcular prejuizo comerciante

valor = float(input('Digite o valor em atraso: '))
acrescimo = valor * 1.10
desc = acrescimo*10/100
preju = valor - desc

print(f'O valor atual a ser pago é de R${preju:.2f} e o prejuízo foi de R$ {desc:.2f}')