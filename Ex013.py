# Acrescimo de 15% no salário inserido

s = float(input('Insira o salário atual: '))
# pode ser feito com: s + (s * 15/100) ao invés de multiplicar por 1.15
print(f'O atual salário do funcionário é R${s:.2f}, com o aumento de 15%, o salário passa a ser de R${(s * 1.15):.2f}')