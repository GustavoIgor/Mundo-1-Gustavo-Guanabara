# Conversão de metros para centímetros e milímetros a partir de um número inserido.

m = float(input('Insira o valor em metros: '))

print(f'A medida é {m} metros, o que corresponde a: '
      f'\n{m/1000}km\n{m/100}hm\n{m/10}dam\n{m*10}dm\n{m*100}cm\n{m*1000}mm')
