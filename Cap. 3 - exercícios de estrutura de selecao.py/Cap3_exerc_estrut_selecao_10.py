#Verificar se é eleitor ativo, facultativo ou não votante

idade = int(input('Insira sua idade: '))

if idade == 16 or idade==17 or idade > 65:
    print('Eleitor facultativo')
elif idade < 16:
    print('Não votante')
elif 18 <= idade <= 65:
    print('Eleitor obrigatório')