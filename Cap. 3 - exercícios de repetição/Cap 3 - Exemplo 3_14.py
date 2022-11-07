#Repetição com seleção de múltipla escolha

tinto = 0
branco = 0
rose = 0
totalvinho = 0
tipovinho = ""

while tipovinho != 'F':
    tipovinho = str(input('Escolha o tipo de vinho: \nPara sair digite (F)'))
    if tipovinho == 'tinto':
        tinto += 1
    elif tipovinho == 'branco':
        branco += 1
    elif tipovinho == 'rose':
        rose += 1
    totalvinho += 1
print(f'{tinto}{branco}{rose}{totalvinho-1}')

portinto = tinto*100/(totalvinho-1)
porbranco = branco*100/(totalvinho-1)
porrose = rose*100/(totalvinho-1)

print(f'Porcentagem tinto: {portinto:.2f}% branco: {porbranco:.2f}% rose: {porrose:.2f}%')