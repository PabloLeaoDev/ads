num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
op = input('Escolha a operação (+, -, *, /): ')

if op == '+':
    print(f'O resultado da soma entre {num1} e {num2} é {num1 + num2}.')
elif op == '-':
    print(f'O resultado da subtração entre {num1} e {num2} é {num1 - num2}.')
elif op == '*':
    print(f'O resultado da multiplicação entre {num1} e {num2} é {num1 * num2}.')
elif op == '/':
    print(f'O resultado da divisão entre {num1} e {num2} é {num1 / num2:.2f}.')
else:
    print('Operação inválida!')