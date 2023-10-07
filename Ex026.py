# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input('Insira uma frase: ').strip()

if(frase.upper().count('A') == 0):
    print(f'A frase "{frase}" não possui a letra "a".')
elif(frase.upper().count('A') == 1):
    print(f'A frase "{frase}" possui apenas uma letra "a" na posição {frase.upper().find("A")}')
else:
    print(f'A frase "{frase}" possui {frase.upper().count("A")} letras A.\nA primeira letra A aparece na posição'
          f' {frase.upper().find("A")}.\nA última letra A aparece na posição {frase.upper().rfind("A")}.')