# Ler um número qualquer e mostrar a porção inteira

from math import trunc

n = float(input('Digite o número para que seja mostrada sua porção inteira: '))

print(f'O numero digitado foi {n}, e sua porção inteira é {trunc(n)}')