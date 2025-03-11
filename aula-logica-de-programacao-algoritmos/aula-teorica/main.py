km = float(input('Quantos km foram percorridos? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
pagar = (dias * 60) + (km * 0.15)
print(f'Você irá pagar R${pagar:.2f} pelo aluguel do carro.')