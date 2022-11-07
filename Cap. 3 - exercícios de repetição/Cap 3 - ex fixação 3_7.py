#Maior e menor número de 20 números
import random
num1 = 0
num2 = 10000000000

for n in range(1,20):
    num = random.randint(1,100)
    print(num)
    if num > num1:
        nummaior = num
        num1 = nummaior
    if num<num2:
        numen = num
        num2 = numen
print(f'Número menor é {numen} e o número maior é {nummaior}')