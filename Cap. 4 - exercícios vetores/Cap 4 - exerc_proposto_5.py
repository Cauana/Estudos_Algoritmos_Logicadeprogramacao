#Exercício precisa de correções

lista = [0,1,2]
listageral = []
lucromenos = []
lucroentre = []
lucromaior = []

for n in range(1,3):
    nome = str(input('Nome: '))
    custo = float(input('Custo: '))
    preco = float(input('preço: '))
    lista[0] = nome
    lista[1] = custo
    lista[2] = preco
    listageral.append(lista)
    
print(listageral)

for p in range(0,2):
    lucro = listageral[p][2]-listageral[p][1]
    print(lucro)
    if lucro < listageral[p][1]*1.1:
        lucromenos.append(lucro)
    elif  listageral[p][1]*1.1 > lucro > listageral[p][1]*1.3:
        lucroentre.append(lucro)
    elif  lucro > listageral[p][1]*1.3:
        lucroentre.append(lucro)
        
print(f'menor que 10% {lucromenos}')
print(f'Lucro entre: {lucroentre}')
print(f'Lucro maior: {lucromaior}')