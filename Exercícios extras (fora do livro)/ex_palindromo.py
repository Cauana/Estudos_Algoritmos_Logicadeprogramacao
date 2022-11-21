#verificar se é um palindromo

#Com método de inversão de string
palavra = str(input('Digite uma palavra ou frase: '))
palavra = palavra.replace(" ","")
print(palavra)
palavrainvertida = palavra[::-1]
print(palavrainvertida)
if palavra == palavrainvertida:
    print('É UM PALÍNDROMO')
else:
    print('NÃO É UM PALÍNDROMO')
    
#Sem uso de método de inversão string   
palavra = str(input('Digite uma palavra ou frase: '))
palavra = palavra.replace(" ","")
invertida = ''
for n in range(len(palavra)):
    invertida = palavra[n] + invertida
print(palavra, invertida)
if palavra == invertida:
    print('É palíndrome')
else:
    print('Não é palíndrome')