#Exercício Cap 3 -  exercício fixação 2.9
n1 = int(input('Digite o número 1: '))
n2 = int(input('Digite o número 2: '))
operacao = str(input('Qual operação deseja realizar? \n(+) : Adição\n'
                     '(-) : Subtração\n'
                     '(*) : Multiplicação\n'
                     '(/) : Divisão\n'))

if operacao == '+': 
    conta = n1 + n2
    print(f'O Resultado de {n1}{operacao}{n2} é {conta}')
elif operacao == '-': 
    conta = n1 - n2
    print(f'O Resultado de {n1}{operacao}{n2} é {conta}')
elif operacao == '*': 
    conta = n1 * n2
    print(f'O Resultado de {n1}{operacao}{n2} é {conta}')
elif operacao == '/': 
    conta = n1 / n2
    print(f'O Resultado de {n1}{operacao}{n2} é {conta}')
else:
    "Favor, insira o símbolo da operação"