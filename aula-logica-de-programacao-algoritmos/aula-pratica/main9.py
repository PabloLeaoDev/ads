strings = (
    "Python",
    "Inteligente",
    "Criatividade",
    "Conhecimento",
    "Aprender",
    "Explorar",
    "Gentileza",
    "Persistência",
    "Imaginação",
    "Tecnologia"
)

def encontrar_vogais(tupla):
    vogais = 'aeiou'
    vogais_ordem = []
    # percorre a tupla
    for word in tupla:
        exibir = []
        exibir.append(word)
        # percorre as strings de cada tupla
        for char in word:
            # averigua se na string tem uma vogal
            if char.lower() in vogais:
                exibir.append(char)
        vogais_ordem.append(exibir)
        # exibir.clear()
    return vogais_ordem

chamada = encontrar_vogais(strings)
print(chamada)