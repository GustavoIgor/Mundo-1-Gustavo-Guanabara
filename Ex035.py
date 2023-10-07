# Recebe 3 comprimentos de retas e diz se elas formam ou não um triângulo

r1 = int(input('Insira o comprimento da primeira reta: '))
r2 = int(input('Insira o comprimento da segunda reta: '))
r3 = int(input('Insira o comprimento da terceira reta: '))

if (r1 < (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < (r1 + r2)):
    print(f'As retas {r1}, {r2} e {r3} formam um triângulo.')
else:
    print(f'As retas {r1}, {r2} e {r3} NÃO formam um triângulo.')