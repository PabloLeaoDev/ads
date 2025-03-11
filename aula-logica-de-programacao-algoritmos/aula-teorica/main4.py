cont = 0
soma = 0
# encontra os valores pares entre 0 e 100
for i in range(0, 101, 2): 
    # conta quantos valores pares foram encontrados
    cont += 1 
    # soma os valores pares
    soma += i 
media = soma / cont
print(f'A média dos valores pares entre 0 e 100 é {media:.2f}.')