#Calculando fatorial

n = int(input('Insira um número para calcular o seu fatorial: '))
count = 1
num = n

for f in range(1, n):
    n = n*count
    count +=1
    
if n == 0:
    n+=1
print(f'{num}! = {n}')
    