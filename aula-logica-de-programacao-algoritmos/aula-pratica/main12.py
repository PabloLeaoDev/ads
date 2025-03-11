import random

def computer_choice(words):
    a = random.randint(0, (len(words) - 1))
    return a

def menu():
    text = 'JOGO DA FORCA'
    print(f'\n{text:-^30}')
    text = 'ESCOLHA'
    print(f'\n{text:_^30}\n')
    print('1. JOGAR\n2. SCORE\n3. SAIR')
    print('_' * 30)
    choice = int(input('\nEscolha a opção de 1 a 3: '))
    return choice

def play(score):
    data_game = []
    player = []
    name = input('Digite o seu nome: ')
    player.append(name)
    punctuation = score
    player.append(punctuation)
    data_game.append(player)
    print(data_game)
    
def op(x):
    match (x):
        case 1:
            print('Vamos jogar!')
            game()
        case 2:
            print('Seu SCORE é...')
        case 3:
            print('Você saiu')
        case _:
            print('Escolha uma opção válida!')

def score(a, c):
    global qtd
    qtd = 1
    flag = True
    while flag:
        if a != c:
            print('Tente novamente! Não se esqueça da acentuação das palavras.')
            qtd += 1
            while True:
                a = input('\nQual a palavra que o computador escolheu? ').upper()
                if a == c:
                    flag = False
                    break
                else:
                    print('Tente novamente! Não se esqueça da acentuação das palavras.')
                    qtd += 1
                    continue
        else:
            print(f'Você conseguiu acertar na {qtd} tentativa!')
            break

def game():
    words = ['Paralelepipedo', 'Matemática', 'Ovos', 'Lógica', 'JavaScript', 'Programação', 'Hacking']
    print('\nA lista de palvras é: ', end='')
    for i in words:
        print(f'{i}', end=' ')
    computer = computer_choice(words)
    computer = words[computer].upper()
    attempt = input('\nQual a palavra que o computador escolheu? ').upper()
    score(attempt, computer)
    play(qtd)
    
def main():
    choice = menu()
    op(choice)
main()