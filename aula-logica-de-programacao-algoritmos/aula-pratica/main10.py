import random
from time import sleep

# função que valida a entrada de dados do usuário
def valida_int(x):
    while True:
        if (x < 1) or (x > 3):
            x = int(input('Digite um valor entre 1 e 3: '))
        else:
            break
    return x

# função que define a escolha do computador
def computer_choice():
    random_number = random.randint(1, 3)
    return random_number

# funçao que é chamada caso o jogador ganhe da máquina
def winner(choice, comp, list = ['PEDRA', 'PAPEL', 'TESOURA']):
    if (choice == 3) and (comp == 2):
        print(f'Você VENCEU para o computador! Ele escolheu {list[comp - 1]} e você {list[choice - 1]}.')
    elif (choice == 2) and (comp == 1):
        print(f'Você VENCEU para o computador! Ele escolheu {list[comp - 1]} e você {list[choice - 1]}.')
    elif (choice == 1) and (comp == 3):
        print(f'Você VENCEU para o computador! Ele escolheu {list[comp - 1]} e você {list[choice - 1]}.')

# funçao que é chamada caso o jogador perca para a máquina
def loser(choice, comp, list = ['PEDRA', 'PAPEL', 'TESOURA']):
    if (choice == 1) and (comp == 2):
        print(f'Você PERDEU para o computador! Ele escolheu {list[comp - 1]} e você {list[choice - 1]}.')
    elif (choice == 2) and (comp == 3):
        print(f'Você PERDEU para o computador! Ele escolheu {list[comp - 1]} e você {list[choice - 1]}.')
    elif (choice == 3) and (comp == 1):
        print(f'Você PERDEU para o computador! Ele escolheu {list[comp - 1]} e você {list[choice - 1]}.')

# funçao que é chamada caso o jogador empate com a máquina
def draw():
    print(f'Você EMPATOU com o computador! Ambos escolheram a mesma opção.')

sleep(.5)
print('\nJO')
sleep(.5)
print('KEN')
sleep(.5)
print('PÔ')
sleep(.5)
print('-' * 15)
print('1. Pedra\n2. Papel\n3. Tesoura')
print('-' * 15)
sleep(1)

machine = computer_choice()
player = valida_int(int(input('Digite um valor entre 1 e 3: ')))

# testes que comparam os valores de player e machine, tendo em vista a derrota do player
test = (player == 1) and (machine == 2)
test1 = (player == 2) and (machine == 3)
test2 = (player == 3) and (machine == 1)

if test or test1 or test2:
    loser(player, machine)
elif (player == machine):
    draw()
else:
    winner(player, machine)