# função que cria uma borda personalizada para a string informada
def border(string):
    if string:
        phrase = len(string)
        print('\n' + '+' + '-' * phrase + '+')
        print('|' + string + '|')
        print('+' + '-' * phrase + '+')
    else:
        print('\nVocê não escreveu uma frase.')
    
border(input('Escreva uma frase: '))