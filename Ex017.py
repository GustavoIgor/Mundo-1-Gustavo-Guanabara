# Cálculo da hipotenusa com dados do cateto adjacente e cateto oposto (h² = co² + ca²)

from math import sqrt, pow
co = float(input('Digite a medida do cateto oposto: '))
ca = float(input('Digite a medida do cateto adjacente: '))

print(f'O valor do cateto oposto é {co} e do cateto adjacente é {ca}, portanto, a hipotenusa é {(sqrt(pow(co, 2) + pow(ca, 2))):.2f}')

# *Também é possivel utilizar o hypot com math.hypot(co, ca)*