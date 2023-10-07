# Recebe o salário e caso ele seja superior a R$1.250,00 o aumento é de 10%, caso o contrário, o aumento é de 15%.

sal = int(input('Insira o salário: '))

if (sal > 1250):
    print(f'Aumento de 10%, o novo salário é de R${(sal * 1.1):.2f}, em comparação com o antigo (R${sal:.2f})')
else:
    print(f'Aumento de 15%, o novo salário é de R${(sal * 1.15):.2f}, em comparação com o antigo (R${sal:.2f})')

