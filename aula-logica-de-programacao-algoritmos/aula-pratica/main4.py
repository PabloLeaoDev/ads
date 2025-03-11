# Tratamento de exceções (maneira sofisticada)
while True:
    try:
        valor = int(input("Digite um valor inteiro positivo: "))
        if valor <= 0:
            raise ValueError("O valor deve ser positivo.")
        print("O valor inteiro positivo inserido foi:", valor)
        break  # Sai do loop se o valor for inteiro positivo
    except ValueError as e:
        print(f"Valor inválido! {e}")