from random import randint
from time import sleep

print('\033[33m-='*30)
print('\033[mVou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('\033[33m-='*30)
num = randint(0, 5)
chute = int(input('\033[mEm que numero eu pensei? '))
print('\033[1;36mPROCESSANDO...')
sleep(1)
if chute == num:
    print(f'\033[1;32mPERDI!\033[m Eu pensei no numero {num} também!')
else:
    print(f'\033[1;31mGANHEI!\033[m Eu pensei no numero {num} e nao no {chute}!')