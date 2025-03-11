games = {'nome': ['Super Mário', 'GTA 5', 'Call of Duty'], 'ano': [1985, 2013, 2023], 'plataforma': ['Nitendo', 'Desktop', 'PlayStation 5']}

for i in range(len(games)):
    # Quando se trata de f-strings e dicionários, precisa-se colocar aspas duplas para referenciar a chave
    print(f'O jogo {games["nome"][i]} foi criado em {games["ano"][i]} e jogado na plataforma {games["plataforma"][i]}')