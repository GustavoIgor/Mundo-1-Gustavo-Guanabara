# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex:
# Digite um número: 1834.
# unidade: 4.
# dezena:3.
# centena:8.
# milhar:1.

n = int(input("Insira um numero de 4 digitos: "))

print(f'Unidade: {n // 1 % 10}\nDezena: {n // 10 % 10}\nCentena: {n // 100 % 10}\nMilhar: {n // 1000 % 10}')