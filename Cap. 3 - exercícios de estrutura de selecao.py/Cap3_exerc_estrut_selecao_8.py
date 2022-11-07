#Se Data existente
dia = int(input('Insira um dia: '))
mes = int(input('Insira um mês: '))
ano = int(input('Insira um ano: '))


if ano%4 == 0 and ano%100 != 0:
    if mes == 2:
        if 0<dia<30:
            print('Data existe')
        else:
            print('Data inválida')
    else:
        print('Data inválida')
    if mes in (1,3,5,7,9,11):
        if 0<dia<32:
            print('Data existe')
        else:
            print('Data inválida')
        if mes in (4,6,8,10,12):
            if 0<dia<31:
                print('Data existe')
            else:
                print('Data inválida')
    else:
        print('Data inválida')
else:
    if mes == 2:
        if 0<dia<29:
            print('Data existe')
        else:
            print('Data inválida')
    else:
            print('Data inválida')
    if mes in (1,3,5,7,9,11):
        if 0<dia<32:
            print('Data existe')
        else:
            print('Data inválida')
    else:
            print('Data inválida')
    if mes in (4,6,8,10,12):
        if 0<dia<31:
            print('Data existe')
        else:
            print('Data inválida')
    else:
            print('Data inválida')