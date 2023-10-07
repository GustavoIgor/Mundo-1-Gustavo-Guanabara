# Recebe distância de uma viagem em km o preço para viagens ATÉ 200km é de R$0,50 por km, mais que isso, R$0,45 por km.

km = int(input('Insira quantos km são percorridos na viagem: '))

if (km > 200):
    print(f'Sua viagem é de mais de 200km, portanto seu preço é de R${(km*0.45):.2f}.')
else:
    print(f'Sua viagem é de menos de 200km, portanto seu preço é de R${(km*0.5):.2f}.')