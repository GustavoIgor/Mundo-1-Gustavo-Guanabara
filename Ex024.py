# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

c = input('Digite o nome da cidade: ').strip()

if(c[:5].upper() == 'SANTO'):
    print(f'A cidade digitada começa com "Santo" ({c}).')
else:
    print(f'A cidade digitada não começa com "Santo" ({c}).')

