#Diferença data atual para data aniversário
diaaniver = int(input('Digite o dia do seu aniversário: '))
mesaniver = int(input('Digite o mês do seu aniversário: '))
anoaniver = int(input('Digite o ano do seu aniversário: '))
dia = int(input('Digite o dia atual: '))
mes = int(input('Digite o mês atual: '))
ano = int(input('Digite o ano atual: '))

anodif = ano-anoaniver
mesdif = mes-mesaniver
diadif = dia-diaaniver

if diadif< 0:
    diadif =0
    mesdif-=1
print(f'A diferença é de {anodif}anos, {mesdif}meses e {diadif}dias')