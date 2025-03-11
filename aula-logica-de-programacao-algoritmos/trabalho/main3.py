print('\n\nBem-vindo a Livraria do Pablo Leão')
def cadastrar_livro(id):
    """Este procedimento coleta os dados de entrada dos usuários, e a partir deles cria um dicionário que é armazenado na lista "lista_livro", para posterior consulta.

    Args:
        id (int): Esse parâmetro é referente ao ID do livro criado pelo usuário.
    """
    
    print(f'Id do livro: {id}')
    nome = input('Por favor, entre com o nome do livro: ')
    autor = input('Por favor, entre com o nome do autor do livro: ')
    editora = input('Por favor, entre com o nome da editora do livro: ')
    dicio = {'ID': id, 'nome': nome, 'autor': autor, 'editora': editora}
    # Armazena na lista "lista_livro" o dicionário "dicio"
    lista_livro.append(dicio)
def consultar_livro():
    """Tal procedimento é responsável por consultar os livros que foram cadastrados, sejam todos eles simultaneamente, seja alguns por meio do ID ou do Autor da obra.
    """
    
    while True:
        # Menu da opção 2, Consultar Livros
        print('1. Consultar Todos')
        print('2. Consultar por ID')
        print('3. Consultar por Autor')
        print('4. Retornar ao menu')
        escolha = int(input('>>'))
        match(escolha):
            # Exibe uma lista de todos os livros cadastrados, com seus respectivos atributos
            case 1:
                for livros in lista_livro:
                    print(f"\nID: {livros['ID']}")
                    print(f"Nome: {livros['nome']}")
                    print(f"Autor: {livros['autor']}")
                    print(f"Editora: {livros['editora']}")
                break
            # Exibe o livro cadastrado com base em seu ID
            case 2:
                id_escolhido = int(input('\nQual o ID que você deseja consultar? '))
                ids_lista = []
                # Percorre a "lista_livro", "i" = dicionários na lista
                for i in lista_livro:
                    # Percorre cada "i", coletando suas chaves e respectivos valores
                    for chaves, valores in i.items():
                        # "value_id" coleta o valor armazenado especificamente na chave "ID" do dicionário, o qual, posteriormente, é armazenado na lista "ids_lista"
                        value_id = i['ID']
                        ids_lista.append(value_id)
                        # Irá exibir na tela caso o ID naquele dicionário específico seja igual ao ID escolhido pelo usuário
                        if chaves == 'ID' and valores == id_escolhido:
                            print(f"\nID: {i['ID']}")
                            print(f"Nome: {i['nome']}")
                            print(f"Autor: {i['autor']}")
                            print(f"Editora: {i['editora']}")
                # Se o ID escolhido pelo usuário não estiver cadastrado, ele exibe uma mensagem alertando isso e repete o loop
                if id_escolhido not in ids_lista:
                    print('\nEsse ID não foi cadastrado. Realize o cadastro ou consulte outro ID!')
                    continue
                break
            # Segue-se no caso 3 a mesma lógica aplicada no caso 2. Contudo, adaptada para fazê-lo com base no autor do livro
            case 3:
                autor_escolhido = input('\nQual o autor que você deseja consultar? ')
                autor_lista = []
                for i in lista_livro:
                    for chaves, valores in i.items():
                        value_autor = i['autor']
                        autor_lista.append(value_autor)
                        if chaves == 'autor' and valores == autor_escolhido:
                            print(f"\nID: {i['ID']}")
                            print(f"Nome: {i['nome']}")
                            print(f"Autor: {i['autor']}")
                            print(f"Editora: {i['editora']}")
                if autor_escolhido not in autor_lista:
                    print('\nEsse autor não foi cadastrado. Realize o cadastro ou consulte outro autor!')
                    continue
                break
            # Para o loop e retorna ao menu principal
            case 4:
                break
            # Caso o usuário não escolha uma opção entre 1 e 4, o loop se repetirá
            case _:
                print('\nOpção inválida! Tente Novamente.')
                continue
def remover_livro():
    """Este procedimento é responsável por remover o livro da base de cadastro, através do ID do mesmo.
    """
    while True:
        id_escolhido = int(input('\nQual o ID do livro que você deseja remover? '))
        ids_lista = []
        # Segue-se aqui a mesma lógica aplicada no caso 2 e 3 contidos no procedimento "consultar_livro()". Entretanto, adaptada para remover o livro escolhido, através do ID, da lista de cadastros
        for i in lista_livro:
            for chaves, valores in i.items():
                value_id = i['ID']
                ids_lista.append(value_id)
                if chaves == 'ID' and valores == id_escolhido:
                    lista_livro.remove(i)
        # Se o ID a ser removido não estiver cadastrado, ele exibe uma mensagem alertando isso e repete o loop
        if id_escolhido not in ids_lista:
            print('\nID inválido! Tente novamente.')
            continue
        break
lista_livro = []
id_global = 0
while True:
    # Menu principal, que apresenta as opções de ações para o usuário
    print('-' * 40)
    print('MENU PRINCIPAL'.center(40, '-'))
    print('Escolha a opção desejada:')
    print('1. Cadastrar Livro')
    print('2. Consultar Livro(s)')
    print('3. Remover Livro')
    print('4. Sair')
    escolha = int(input('>>'))
    print('-' * 40)
    # Realiza um determinado processo com base na escolha do usuário
    match(escolha):
        case 1:
            identificador = int(input('\nQual o ID do livro que você deseja cadastrar? '))
            id_global = identificador
            # Utiliza o "id_global" como argumento ao chamar a função "cadastrar_livro()"
            cadastrar_livro(id_global)
        case 2:
            consultar_livro()
        case 3:
            remover_livro()
        case 4:
            break
        # Caso o usuário não escolha uma opção entre 1 e 4, o loop se repetirá
        case _:
            print('\nOpção inválida! Tente Novamente.')
            continue