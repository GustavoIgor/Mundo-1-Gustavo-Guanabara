# Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

nome = input('Insira o seu nome: ').strip()
print(f'Seu nome em maiúsculas é {nome.upper()}.')
print(f'Seu nome em minúsculas é {nome.lower()}.')
print(f'Seu nome ao todo tem {len(nome.replace(" ", ""))} letras.') # ou len(nome) - nome.count(" ")
print(f'Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.')
