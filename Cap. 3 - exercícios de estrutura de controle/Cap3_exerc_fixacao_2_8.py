#Exercício Cap 3 -  exercício fixação 2.8
preco = float(input('Digite o preço: '))
condicao = int(input('Digite a condição de pagamento: \n1 - À vista em dinheiro ou cheque, recebe 10%, de desconto\n'
                     '2 - À vista no cartão de crédito, recebe 5%, de desconto\n'
                     '3 - Em duas vezes, preço normal da etiqueta sem juros\n'
                     '4 - Em três vezes, preço normal de etiqueta mais juros de 10%\n\n'))

if condicao == 1: 
    preco = preco * 0.9
    print(f'O valor final a ser pago é: R${preco:.2f} ')
elif condicao == 2:
    preco = preco * 0.95
    print(f'O valor final a ser pago é: R${preco:.2f} ')
elif condicao == 3:
    precomes = preco/2
    print(f'O valor final a ser pago é: R${preco:.2f} em 2 meses por {precomes:.2f}')
elif condicao == 4:
    preco=preco*1.10
    precomes = preco/3
    print(f'O valor final a ser pago é: R${preco:.2f} em 3 meses por {precomes:.2f}')
