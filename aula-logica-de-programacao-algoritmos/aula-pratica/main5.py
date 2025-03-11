print('LANCHONETE')
print('-' * 10)
print('1 - Coxinha R$ 5,00')
print('2 - Café R$ 7,00')
print('3 - Pastel R$ 4,00')
print('4 - Suco R$ 6,00')
print('5 - SAIR')
print('-' * 10)

valorPagar = 0
while True:
    op = int(input('\nEscolha sua opção: '))
    if (op >= 1 and op <= 4):
        qtd = int(input('Quantas unidades deseja comprar? '))
        if (op == 1):
            valorPagar += 5 * qtd
        elif (op == 2):
            valorPagar += 7 * qtd
        elif (op == 3):
            valorPagar += 4 * qtd
        elif (op == 4):
            valorPagar += 6 * qtd
        print('Pedido adicionado!')
    else:
        if (op == 5):
            break
        else:
            print('Opção inválido!')
print(f'\nO valor total a ser pago é de R${valorPagar:.2f}')