#Verificação se é um número primo, utilizando for com incremento

count = 0
n = int(input('Insira um número: '))
for d in range(1,n+1):
    if n%d == 0:
        count +=1
        print(f'O número {n} é divisivel por {d}')
if count > 2:
    print('Não é número primo')
else: 
    print('É número primo')