#Consumo efetuado, autonomia - dado capacidade tanque, qtdade litros abastecidos e a km percorrido desde o ultimo abastecimento
captanque = int(input('Capacidade do tanque: '))
qtdadelitros = int(input('Quantidade de litros abastecido: '))
km = int(input('Quilometros andados: '))

consumorestante = captanque - qtdadelitros
kmporl = km/qtdadelitros
autonomia = consumorestante/kmporl

print(f'O consumo efetuado foi de {qtdadelitros} Litros, autonomia que o carro teria é de {autonomia} KM')