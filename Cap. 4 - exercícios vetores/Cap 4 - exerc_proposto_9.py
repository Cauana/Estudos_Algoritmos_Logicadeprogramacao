#calculo de moda de um conjunto

n = [0,1,2,3,5,6,2,3,5,2,2,1,4,2,2,5,6]
maiorqtdade = 0

for i in range(len(n)):
    qtdade = n.count(i)
    if maiorqtdade<= qtdade:
        maiorqtdade = qtdade
        num = i
print(f'A moda é {num}')