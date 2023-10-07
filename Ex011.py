# Ler largura e altura de uma parede em metros e calcular a área e a quantidade de tinta necessária
# cada litro de tinta pinta uma área de 2m²

l = float(input('Insira a largura da parede em metros: '))
a = float(input('Insira a altura da parede em metros: '))

print(f'Considerando que a largura da parede é {l}m e a altura {a}m, sua área é de {l*a}m².'
      f' Como cada litro de tinta pinta 2m², serão necessários {(l*a) / 2}l de tinta para pintá-la.')