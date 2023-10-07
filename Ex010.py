# Converter valor recebido para dólares (Considerando US$1,00 = R$5,04, no dia 1º de outubro de 2023)

r = float(input('Insira o valor em reais: '))

print(f'O valor em reais é R${r:.2f}, a cotação do dólar está em R$5,04, portanto, o valor em dólares é US${(r / 5.04):.2f}.')