import time;

print('Determine os lados de um Triângulo:')
print('------------------------------------')
time.sleep(1)
while True:
    a = float(input('\nLado A: '))
    b = float(input('Lado B: '))
    c = float(input('Lado C: '))

    if (a > b + c) or (b > a + c) or (c > a + b) and (a <= 0) or (b <= 0) or (c <= 0):
        print('\nTriângulo Inválido.\nTente novamente, com outros valores para os lados.')
        time.sleep(1)
    else:
        # Verifica qual o tipo de triângulo, pois ele é válido
        if (a == b == c):
            print('\nO triângulo é do tipo: Equilátero.')
            break
        elif (a == b or b == c or c == a):
            print('\nO triângulo é do tipo: Isósceles.')
            break
        else:
            print('\nO triângulo é do tipo: Escaleno.')
            break
