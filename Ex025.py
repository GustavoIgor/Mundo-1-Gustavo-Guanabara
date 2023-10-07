# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = input('Digite um nome completo: ').strip()

if ('SILVA' in nome.upper()):
    print(f'O nome possuí Silva ({nome}).')
else:
    print(f'O nome NÃO possui Silva ({nome}).')