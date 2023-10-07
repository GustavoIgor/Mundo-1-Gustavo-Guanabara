nome = input("Qual seu nome? ")

if nome == 'Gustavo':
    print('Salve!')
else:
    print('NÃO Salve!')

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
m = (n1 + n2) / 2

if m < 6:
    print(f'Você teve nota {m:.2f}, REPROVADO!')
else:
    print(f'Você teve nota {m:.2f}, PASSOU DE ANO.')

# Aula necessária para os exercícios do 28 até o 35.