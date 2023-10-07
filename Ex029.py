# Ler a velocidade de um carro em km/h. Se ultrapassar 80km/h, há multa. 7 reais por cada km/h ultrapassado.

vel = int(input('Quantos km/h o carro estava? '))

if(vel > 80):
    print(f'Infelizmente o limite de 80km/h foi ultrapassado, terá de pagar R${((vel - 80) * 7):.2f}.')
else:
    print(f'Sua velocidade foi de {vel}km/h, o que está dentro do limite de velocidade (80km/h).')