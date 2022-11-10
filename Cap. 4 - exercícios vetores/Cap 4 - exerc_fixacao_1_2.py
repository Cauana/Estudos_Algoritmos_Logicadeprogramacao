#operações entre vetores

lista1 = [2,4,6,8,10]
lista2 = [12,14,16,18,20]
listasoma = []
listasubtracao = []
listamultiplicacao = []
listadivisao = []

for item in range(0,5):
    listasoma.append(lista1[item]+lista2[item])
    listasubtracao.append(lista2[item]-lista1[item])
    listamultiplicacao.append(lista1[item]*lista2[item])
    listadivisao.append(lista2[item]/lista1[item])
print(listasoma)
print(listasubtracao)
print(listamultiplicacao)
print(listadivisao)