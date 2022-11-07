#Soma de H utilizando while com decremento

n = int(input('Insira um número: '))
count = n
H = 0
while count > 0:
    H = H + (1/n)
    print(H)
    count -= 1
    n -= 1
