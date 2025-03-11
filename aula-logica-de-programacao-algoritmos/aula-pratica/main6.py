# 100, 50, 20 ,10, 5, 2, 1
valor = int(input('Qual valor deseja sacar? '))
qtd = 0
while True:
    if valor >= 100:
        cedulas = valor // 100
        print(f'Voce receberá {cedulas} notas de 100')
        valor = valor % 100
    if valor >= 50:
        cedulas = valor // 50
        print(f'Voce receberá {cedulas} notas de 50')
        valor = valor % 50
    if valor >= 20:
        cedulas = valor // 20
        print(f'Voce receberá {cedulas} notas de 20')
        valor = valor % 20
    if valor >= 10:
        cedulas = valor // 10
        print(f'Voce receberá {cedulas} notas de 10')
        valor = valor % 10
    if valor >= 5:
        cedulas = valor // 5
        print(f'Voce receberá {cedulas} notas de 5')
        valor = valor % 5
    if valor:
        cedulas = valor // 1
        print(f'Voce receberá {cedulas} notas de 1')
    break