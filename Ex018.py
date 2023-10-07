# Ler um ângulo qualquer e mostrar o valor do seno, cosseno e tangente

from math import radians, sin, cos, tan
a = (float(input('Insira o angulo desejado: ')))

print(f'O angulo de {a:.2f}º tem seno de {sin(radians(a)):.2f}')
print(f'O angulo de {a:.2f}º tem cosseno de {cos(radians(a)):.2f}')
print(f'O angulo de {a:.2f}º tem tangente de {tan(radians(a)):.2f}')

