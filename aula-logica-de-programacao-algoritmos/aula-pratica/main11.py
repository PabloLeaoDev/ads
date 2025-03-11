import datetime

dicio = {}
cont = 0
flag = True
# uma variável glogal que armazena o ano atual
global year
year = datetime.datetime.now().year

def average_age(dicio):
    """This function calculate the average age of registered users, and return the value.

    Returns:
        float: returns the average age of registered users.
    """
    for value in dicio.values():
        x = value[1]
        age = year - x
        age += age
    global average
    average = age / (cont)
    return average

def young_woman(dicio):
    """This function calculate the age of women registered and return a list with the name of below thirty years old woman.

    Args:
        dicio (dict): A dictionary with the data of registered people.

    Returns:
        list: A list with the name of below thirty years old woman.
    """
    lower = []
    for value in dicio.values():
        x = value[2]
        if x.upper() == 'F':
            y = value[1]
            age = year - y
            if age < 30:
                lower.append(value[0])
    return lower

def above_men(dicio):
    """This function calculate the age of registered man and return a list with the name of above average age registered people men.

    Args:
        dicio (dict): A dictionary with the data of registered people.

    Returns:
        list: A list with the name of above average age registered people men.
    """
    above = []
    for value in dicio.values():
        x = value[2]
        if x.upper() == 'M':
            y = value[1]
            age = year - y
            if age > average:
                above.append(value[0])
    return above

while flag:
    user = []
    name = input('\nDigite seu nome: ')
    birth = int(input('Digite o ano do seu nascimento: '))
    sex = input('Digite qual é o seu sexo: [M/F] ')
    user.append(name)
    user.append(birth)
    user.append(sex)
    dicio[f'user{cont}'] = user
    cont += 1
    again = input('\nDeseja cadastrar mais alguém? [S/N] ')
    
    while True:
        if again.upper() == 'S':
            break
        elif again.upper() == 'N':
            flag = False
            break
        else:
            print('\nDigite um valor válido!')
            again = input('Deseja cadastrar mais alguém? [S/N] ')
print(f'\n\nO total de cadastros efetuados foi de {cont}.')
media = average_age(dicio)
print(f'A média da idade dos cadastrados é de {media:.2f}.')
women = young_woman(dicio)
print(f'Lista de mulheres cadastradas com menos de 30 anos: {women}.')
men = above_men(dicio)
print(f'Lista de homens cadastrados com a idade acima da média obtida: {men}.')