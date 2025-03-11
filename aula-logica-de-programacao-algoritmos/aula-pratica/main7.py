# < 3 não paga, 3 > e < 12 paga R$15, > 12 paga R$ 30
totalUsers = 0
price = 0
ageUsers = 0
flag = True # uma flag para parar o loop
while flag:
    user = int(input('Qual é a sua idade? '))
    if (user < 3):
        print('Ingresso gratuitos!')
        ageUsers += user
    elif (user >= 3 and user < 12):
        print('Ingresso de R$ 15,00')
        ageUsers += user
        price += 15
    else:
        print('Ingresso de R$ 30,00')
        ageUsers += user
        price += 30
    totalUsers += 1
    op = input('Deseja continuar? [S/N] ').upper()
    if (op == 'S'):
        continue
    elif (op == 'N'):
        print(f'\n\nTotal de ingressos vendidos: {totalUsers}\nMedia da idade dos compradores: {ageUsers / totalUsers:.2f}\nTotal arrecadado: R${price:.2f}')
        break
    else:
        while True:
            print('Opção inválida. Tente novamente!')
            op = input('Deseja continuar? [S/N] ').upper()
            if (op == 'S'):
                break
            elif (op == 'N'):
                flag = False
                break
        if not flag: # se o flag for falso deve parar o loop principal
            print(f'\n\nTotal de ingressos vendidos: {totalUsers}\nMedia da idade dos compradores: {ageUsers / totalUsers:.2f}\nTotal arrecadado: R${price:.2f}')
            break