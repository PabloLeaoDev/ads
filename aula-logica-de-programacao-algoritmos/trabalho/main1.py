def menu():
    print('Bem-vindo a Loja de Gelados do Pablo Leão')
    print('CARDÁPIO'.center(46, '-'))
    print('---| Tamanho | Cupuaçu (CP) |  Açaí (AC)  |---')
    print('---|    P    |   R$  9.00   |  R$ 11.00   |---')
    print('---|    M    |   R$ 14.00   |  R$ 16.00   |---')
    print('---|    G    |   R$ 18.00   |  R$ 20.00   |---')
    print(f'-' * 46)
    return escolher()
def escolher():
    flag = True
    # "pedidos" irá receber uma lista para cada pedido que o usuário fizer
    pedidos = []
    while flag:
        sabor_escolhido = input('Entre com o sabor desejado (CP/AC): ').upper()
        tipo = ('CP', 'AC')
        # Se "sabor" não estiver em "tipo"
        if sabor_escolhido not in tipo:
            print('Sabor inválido. Tente novamente.\n')
            continue
        while True:
            tamanho_escolhido = input('Entre com o tamanho desejado (P/M/G): ').upper()
            # Pequeno, Médio e Grande
            size = ('P', 'M', 'G')
            # Se "tamanho" não estiver em "size"
            if tamanho_escolhido not in size:
                print('Tamanho inválido. Tente novamente.\n')
                continue
            else:
                op_cp = f'Você escolheu Cupuaçu de tamanho {tamanho_escolhido}: R$'
                op_ac = f'Você escolheu Açaí de tamanho {tamanho_escolhido}: R$'
                if sabor_escolhido == 'CP':
                    if tamanho_escolhido == 'P':
                        print(op_cp, '9.00')
                    elif tamanho_escolhido == 'M':
                        print(op_cp, '14.00')
                    else:
                        print(op_cp, '18.00')
                else:
                    if tamanho_escolhido == 'P':
                        print(op_ac, '11.00')
                    elif tamanho_escolhido == 'M':
                        print(op_ac, '16.00')
                    else:
                        print(op_ac, '20.00')
                pedidos.append((sabor_escolhido, tamanho_escolhido))
                if input('\nDeseja mais alguma coisa (S/N)? ').upper() == 'S':
                    break
                else:
                    # Essa condição irá parar as duas iterações, por meio da "flag"
                    flag = False
                    break
    return pedidos
def calcular_valor(pedidos):
    custo_total = 0
    # "sabor" e "tamanho" irá armazenar os respectivos valores em cada lista contida em "pedidos"
    for sabor, tamanho in pedidos:
        if sabor == 'AC':
            # valor_caso_verdadeiro if condição elsevalor_caso_falso
            custo_total += 11 if tamanho == 'P' else (16 if tamanho == 'M' else 20) 
        # Essa condição representa a opção Cupuaçu
        else:
            custo_total += 9 if tamanho == 'P' else (14 if tamanho == 'M' else 20)
    return custo_total
def main():
    pedidos = menu()
    pagar = (f'{calcular_valor(pedidos):.2f}')
    print(f'\nO valor total a ser pago é de R${pagar}')
main()