#divisão sem utilizar / ou div

num = int(input('Digite o número que deseja dividir: '))
divisor = int(input('Insira o divisor: '))
count = 1
total = 0
while total < num:
    total +=divisor
    count+=1
print(count-1)