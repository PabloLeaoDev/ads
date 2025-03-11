frase = input('Escreva uma frase qualquer: ')
# encontra a metade da frase
separador = len(frase) // 2
# cria a primeira metade da frase
frase2 = frase[:separador]
print(frase2)
# separa os dois últimos caracteres da primeira metade da frase
frase3 = frase2[-2:]
print(frase3)