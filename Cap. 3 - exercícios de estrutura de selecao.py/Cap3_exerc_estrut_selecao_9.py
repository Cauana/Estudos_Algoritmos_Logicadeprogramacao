#Se Data existente
dia = int(input('Insira um dia: '))
mes = str(input('Insira um mês: '))

if dia >= 21 and mes == 'março' or mes == 'abril' and dia <=20:
    print('Signo de Áries')
if dia >= 21 and mes == 'abril' or mes == 'maio' and dia <=20:
    print('Signo de Touro')
if dia >= 21 and mes == 'maio' or mes == 'junho' and dia <=20:
    print('Signo de Gêmeos')
if dia >= 21 and mes == 'junho' or mes == 'julho' and dia <=22:
    print('Signo de Câncer')
if dia >= 23 and mes == 'julho' or mes == 'agosto' and dia <=22:
    print('Signo de Leão')
if dia >= 23 and mes == 'agosto' or mes == 'setembro' and dia <=22:
    print('Signo de Virgem')
if dia >= 23 and mes == 'setembro' or mes == 'outubro' and dia <=22:
    print('Signo de Libra')
if dia >= 23 and mes == 'outubro' or mes == 'novembro' and dia <=21:
    print('Signo de Escorpião')
if dia >= 22 and mes == 'novembro' or mes == 'dezembro' and dia <=21:
    print('Signo de Sagitário')
if dia >= 22 and mes == 'dezembro' or mes == 'janeiro' and dia <=20:
    print('Signo de Capricórnio')
if dia >= 21 and mes == 'janeiro' or mes == 'fevereiro' and dia <=19:
    print('Signo de Aquário')
if dia >= 19 and mes == 'fevereiro' or mes == 'março' and dia <=20:
    print('Signo de Aquário')