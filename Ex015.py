# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

d = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))

print(f'Sabendo que o carro foi alugado por {d} dias e foram rodados {km}km, o total a se pagar é R${((60 * d)+(0.15*km)):.2f}')