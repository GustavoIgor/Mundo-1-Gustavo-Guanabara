#Ler 3 números e mostrar qual é o maior e qual é o menor

n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))
maior = n1
menor = n1

if (n2 > n1) and (n2 > n3):
    maior = n2
if (n3 > n1) and (n3 > n2):
    maior = n3

if (n2 < n1) and (n2 < n3):
    menor = n2
if (n3 < n1) and (n3 < n2):
    menor = n3

print(f'O menor número digitado foi {menor} e o maior o {maior}')