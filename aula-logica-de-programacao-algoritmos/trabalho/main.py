def menu():
    """Função que exibe o menu, recebe os dados e os processa, através da multiplicação do preço do produto e da quantidade comprada.
    """
    
    print('Bem-vindo a Loja do Pablo Leão')
    valor = float(input('Entre com o valor do produto: '))
    qtd = float(input('Entre com a quantidade do produto: '))
    # variável que armazena o valor total da compra, tendo em vista o valor unitário do produto e a quantidade comprada do mesmo
    valorFinal = valor * qtd
    aplicarDesconto(valorFinal)
def aplicarDesconto(valor):
    """Função que aplica uma porcentagem de desconto com base no valor final da compra.

    Args:
        valor (float): valor final da compra.
    """
    
    # Se valor for menor que 2500 o desconto será de 0%
    if (valor < 2500):
        valorDesconto = 0
    # Se valor for igual ou maior que 2500 e menor que 6000 o desconto será de 4%
    elif (valor >= 2500 and valor < 6000):
        valorDesconto = valor - (valor * 0.04)
    # Se valor for igual ou maior que 6000 e menor que 10000 o desconto será de 7%
    elif (valor >= 6000 and valor < 10000):
        valorDesconto = valor - (valor * 0.07)
    # Se valor for igual ou maior que 10000 o desconto será de 11%
    elif (valor >= 10000):
        valorDesconto = valor - (valor * 0.11)
    else:
        print('Houve um erro!')
    exibirValores(valor, valorDesconto)
def exibirValores(valorInicial, valorFinal):
    """Função que exibe os valores sem desconto e com desconto, caso tenha, no terminal.

    Args:
        valorInicial (float): valor total da compra.
        valorFinal (float): valor final da compra, com desconto.
    """
    
    print(f'Valor SEM desconto: R${valorInicial:.2f}')
    # Se valorFinal != 0, ou seja, "Truth"
    if valorFinal:
        print(f'Valor COM desconto: R${valorFinal:.2f}')
    else:
        print('Não há desconto para valores abaixo de R$2500!')
def main():
    """Função principal, responsável por chamar a função "menu()".
    """
    
    menu()
main()