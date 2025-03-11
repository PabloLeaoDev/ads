def menu():
    # O menu descritivo, com as respectivas opções de serviços.
    print('Bem-vindo a Copiadora do Pablo Leão')
    print('\nEntre com o tipo de serviço desejado')
    print('DIG - Digitalização')
    print('ICO - Impressão Colorida')
    print('IPB - Impressão Preto e Branco')
    print('FOT - Fotocópia')
def escolha_servico():
    op = ('DIG', 'ICO', 'IPB', 'FOT')
    while True:
        servico = input('>>').upper()
        # Se "servico" está na tupla "op", o loop será parado
        if servico in op:
            break
        # Se não, exibe uma mensagem para fazer com que o usuário digite uma opção válida.
        else:
            print('Escolha inválida. Entre com o tipo do serviço novamente.')
    return servico
def num_pagina():
    servico = escolha_servico()
    global paginas
    global desconto
    global preco
    while True:
        # É um loop que tenta receber um valor válido de páginas, se o valor ultrapassar 19999 ou se o valor não for um número inteiro, ele pede para o usuário digitar algo válido. O loop finaliza somente quando receber tal valor.
        try:
            paginas = int(input('Entre com o número de páginas: '))
            if paginas >= 20000:
                print('Não aceitamos tantas páginas de uma vez.\nPor favor, entre com o número de páginas novamente.')
            else:
                break
        except ValueError:
            print('Digite um número inteiro.')
    # As condições abaixo atribuem um valor específico a "desconto", dependendo do número de páginas.
    if paginas < 20:
        desconto = 0
    elif paginas >= 20 and paginas < 200:
        desconto = 0.15
    elif paginas >= 200 and paginas < 2000:
        desconto = 0.20
    elif paginas >= 2000 and paginas < 20000:
        desconto = 0.25
    # As condições abaixo atribuem o preço correto ao serviço escolhido, e calculam o valor que deve ser pago, com base no serviço e  no número de páginas, aplicando o desconto.
    if servico == 'DIG':
        preco = 1.1
        pagar = paginas * preco
        pagar = pagar - (pagar * desconto)
    elif servico == 'ICO':
        preco = 1
        pagar = paginas * preco
        pagar = pagar - (pagar * desconto)
    elif servico == 'IPB':
        preco = 0.4
        pagar = paginas * preco
        pagar = pagar - (pagar * desconto)
    elif servico == 'FOT':
        preco = 0.2
        pagar = paginas * preco
        pagar = pagar - (pagar * desconto)
    return pagar
def servico_extra():
    # Um submenu, com as possíveis opções de serviços a mais. Inclusive, dando a opção de não escolher serviço extra algum.
    print('\nDeseja adicionar algum serviço?')
    print('1 - Encardenação Simples - R$ 15.00')
    print('2 - Encardenação Capa Dura - R$ 40.00')
    print('0 - Não desejo mais nada.')
    global adicional
    # Um loop com a estrutura "match/case" que atribui um preço, ou não, dependendo da opção escolhida pelo usuário. Caso a opção escolhida pelo usuário não esteja no escopo adequado (0, 1 e 2), ele deverá escolher um valor válido para sair da repetição.
    while True:
        extra = int(input('>>'))
        match (extra):
            case 1:
                adicional = 15
                break
            case 2:
                adicional = 40
                break
            case 0:
                adicional = 0
                break
            case _:
                print('Escolha inválida. Entre com o tipo do serviço adicional novamente.')
                continue
    return adicional
# MAIN
menu()
descontado = num_pagina()
extra = servico_extra()
# Calcula o preço total a ser pago, de acordo com o pedido.
total_pagar = descontado + extra
# Se há desconto e adicional, execute o "print" mostrando o quanto foi descontado e o valor adicionado. Se não há, não mostre nenhum desconto ou adição no "print".
if desconto and adicional:
    print(f'Total: R$ {total_pagar:.2f} (serviço: {preco:.2f} * páginas: {paginas} com {desconto}% de desconto + extra: R$ {adicional:.2f})')
elif desconto: 
    print(f'Total: R$ {total_pagar:.2f} (serviço: {preco:.2f} * páginas: {paginas} com {desconto}% de desconto')
elif adicional:
    print(f'Total: R$ {total_pagar:.2f} (serviço: {preco:.2f} * páginas: {paginas} + extra: R$ {adicional:.2f})')
else:
    print(f'Total: R$ {total_pagar:.2f} (serviço: {preco:.2f} * páginas: {paginas})')