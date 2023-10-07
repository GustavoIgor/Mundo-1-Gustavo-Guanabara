# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('Insira o primeiro aluno: ')
a2 = input('Insira o segundo aluno: ')
a3 = input('Insira o terceiro aluno: ')
a4 = input('Insira o quarto aluno: ')

lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'A ordem sorteada de apresentação será: {lista}')