# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input('Insira um nome completo: ').strip()
print(f'O primeiro nome é {nome.split()[0]}.\nE o último nome é {nome.split()[len(nome.split()) - 1]}.')