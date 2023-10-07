# Joguinho de adivinhação com um numero entre 0 e 5

from random import randint
from time import sleep
num = randint(0, 5)

chute = int(input('Pensei em um número entre 0 e 5, tente adivinhar: '))
print('Vamos ver...')
sleep(2)
if(chute == num):
    print(f'\033[32;40mParabéns, o número realmente era {num}!\033[m')
else:
    print(f'\033[31;40mQue pena... eu pensei no número {num}!\033[m')