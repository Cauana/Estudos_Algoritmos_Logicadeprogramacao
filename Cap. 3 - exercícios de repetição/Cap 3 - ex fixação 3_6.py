#Série de Fibonacci até 20º termo

n1 = 1
n2 = 1
print(f'{n1}\n{n2}')

for f in range(1,7):
    n3 = n1 + n2
    print(n3)
    n1 = n2 + n3
    print(n1)
    n2 = n3+n1
    print(n2)
    