def somente_positivos(num):
    """Function that validates whether the value passed by the user is positive, if so, it calls the "factorial()" function. If it is not positive, it repeats the request until the user grants a valid value.

    Args:
        num (int): value that the user chose to perform the factorial operation.
    """
    
    flag = True
    while flag:
        if num >= 0:
            fatorial(num)
            break
        else:
            while True:
                num = int(input('\nDigite um valor positivo, por favor: '))
                if num >= 0:
                    flag = False
                    fatorial(num)
                    break
                else:
                    print('\nO valor deve ser positivo. Tente novamente!')
                
def fatorial(valor):
    """Function that calculate de factorial value.

    Args:
        valor (int): value taken in the "somente_positivos()" function.
    """
    
    f = 1
    if valor == 0:
        print(f)
    else:
        for c in range(valor, 0, -1):
            print(f'{c}! ', end='')
            f *= c
        print(f' = {f}')

n = int(input('Digite um valor positivo pata calcular a fatorial: '))
somente_positivos(n)