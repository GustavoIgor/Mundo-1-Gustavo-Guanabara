# Tabuada de um número inteiro qualquer

n = int(input('Insira o número que deseja saber a tabuada: '))
print('='*12)
for x in range(10):
    print(f'{n} X {(x+1):2} = {n*(x+1)}')
print('='*12)