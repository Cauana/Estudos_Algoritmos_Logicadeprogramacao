#Inverter a ordem dos digitos, unidade, centena e dezena
num = int(input('Digite um número de 3 dígitos: '))
cent = int(num/100)
dez = int((num - cent*100)/10)
unidade = int(num - (cent*100) - (dez * 10))

print(unidade,dez,cent)