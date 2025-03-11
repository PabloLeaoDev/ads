# Thuthy and Falsey (True and False)
# Em python, 0 e string vazia é Falsey (outro nome para False). Todo resto é Truthy (outro nome para True).

nome = '' # Falsey
while not nome:
    nome = input('Qual é o seu nome? ')
    if not nome:
        continue # volta para o loop
valor = int(input('Qual é o valor? '))
if valor:
    print('Seu valor é diferente de zero.')
else:
    print('Seu valor é zero.')