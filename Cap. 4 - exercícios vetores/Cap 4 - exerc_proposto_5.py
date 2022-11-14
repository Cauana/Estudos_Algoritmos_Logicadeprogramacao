#Exercício precisa de correções
#Dúvida
listanome = []
listapreco = []
listacusto = []
lucromenos = []
lucroentre = []
lucromaior = []

for n in range(1,3):
    nome = str(input('Nome: '))
    custo = float(input('Custo: '))
    preco = float(input('preço: '))
    listanome.append(nome)
    listacusto.append(custo)
    listapreco.append(preco)

for p in range(0,2):
    lucro = listapreco[p]-listacusto[p]
    print(f'Lucro = {lucro}')
    print(lucro)
    if lucro+listacusto[p] <= listacusto[p]*1.1:
        print(f'O produto {listanome[p]} teve lucro de {lucro} menor do que 10%.\nPreço = R${listapreco[p]} e custo = R${listacusto[p]}')
    elif  listacusto[p]*1.1 < lucro+listacusto[p] < listacusto[p]*1.3:
        print(f'O produto {listanome[p]} teve lucro de {lucro} entre 10% e 30%.\nPreço = R${listapreco[p]} e custo = R${listacusto[p]}')
    elif  lucro+listacusto[p] > listacusto[p]*1.3:
        print(f'O produto {listanome[p]} teve lucro de {lucro} maior do que 30%.\nPreço = R${listapreco[p]} e custo = R${listacusto[p]}')
