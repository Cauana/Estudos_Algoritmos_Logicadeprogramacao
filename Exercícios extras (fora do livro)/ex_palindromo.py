#verificar se é um palindromo

palavra = str(input('Digite uma palavra ou frase: '))
palavra = palavra.replace(" ","")
print(palavra)
palavrainvertida = palavra[::-1]
print(palavrainvertida)
if palavra == palavrainvertida:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')