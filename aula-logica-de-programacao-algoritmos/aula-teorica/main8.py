# lambda é um tipo de função simples, escrita em uma linha. Sintaxe: lambda (argumentos):(retorno)
res = lambda x, y: (x + 5) * y

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
print(f'O resultado é do cálculo de {a} + 5 vezes {b} é {res(a, b)}')