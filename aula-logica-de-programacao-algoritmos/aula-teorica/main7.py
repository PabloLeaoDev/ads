def phrase(string = '', min = 0, max = 30):
    global x
    x = len(string)
    if min < 0 or max < 0:
        print('O número minimo e o maximo devem ser positivos.')
    elif max < min:
        print('O número maximo deve ser maior que o minimo.')
    else:
        if x >= min and x <= max:
            return True
        else:
            return False

frase = input('Escreva uma frase qualquer: ')
numMin = int(input('Escreva o número minímo de caracteres que a frase deve possuir: '))
numMax = int(input('Escreva o número máximo de caracteres que a frase deve possuir: '))
pull = phrase(frase, numMin, numMax)

if pull:
    print(f'A frase: "{frase}" é válida e tem {x} caracteres.')
else:
    print(f'A frase: "{frase}" não é válida.')