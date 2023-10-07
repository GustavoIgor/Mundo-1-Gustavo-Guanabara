# Recebe um ano qualquer e verifica se é um ano bissexto
from datetime import date
ano = int(input('Insira um ano qualquer (0 para o ano atual): '))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto')
else:
    print(f'0 ano {ano} não é bissexto')