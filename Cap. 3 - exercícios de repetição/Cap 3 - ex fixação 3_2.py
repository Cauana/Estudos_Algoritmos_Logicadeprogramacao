#While not - valor aproximado de raíz quadrada

#conferindo o valor da raíz quadrada, para confirmar
n = int(input('Insira um número: '))
raiz = n ** 0.5
print(raiz)

#valor aproximado da raíz usando while not
r = 0
while not (r*r)>=n:
    r +=1
print (f'O valor aproximado da raíz quadrada de {n} é {r}')