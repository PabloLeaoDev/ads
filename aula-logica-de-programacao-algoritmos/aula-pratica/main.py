import time

preco = float(input('Digite o preço do seu produto: R$'))
# cria um delay de meio segundo
time.sleep(0.5)
escolha = int(input('Escolha um valor de desconto (0-100%): '))
print(f'Você receberá {escolha}% de desconto! ')
time.sleep(0.5)
# calcula o desconto
desconto = (preco * escolha) / 100
# calcula o valor final
preco_final = preco - desconto
print(f'Você irá pagar R${preco_final:.2f}')