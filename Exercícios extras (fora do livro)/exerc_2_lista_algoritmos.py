#Agora usando listas, indique como um troco deve ser dado utilizando-se um número mínimo de
#notas. Seu algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado
#desprezando os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1
#reais, e que nenhuma delas esteja em falta no caixa.
menorqt = 9000000000000
valorconta = int(input('Valor da conta: '))
valordopagamento = int(input('Valor do pagamento: '))

troconecessario = valordopagamento-valorconta

notas = [50,20,10,5,2,1]

for i in range(len(notas)):
    qtdadenota = troconecessario//notas[i]
    if qtdadenota == 0:
        qtdadenota = 0
        continue
    elif troconecessario < notas[i] and troconecessario!=0:
        troconecessario = int(notas[i])-troconecessario
    else:
        troconecessario = int(troconecessario)-notas[i]
    print(f'{qtdadenota} notas de {notas[i]} reais')
    