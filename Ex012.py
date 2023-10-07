# Aplicar 5% de desconto no valor digitado

p = float(input('Insira o valor do produto: '))
# Pode ser feito com p - (p * 5/100) ao invés de multiplicar por 0.95.
print(f'O valor do produto é R${p:.2f}, após o desconto de 5%, seu valor passa a ser R${(p * 0.95):.2f}.')