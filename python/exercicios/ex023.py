from time import sleep
num = int(input('\033[33mInform um numero: '))
numero = str(num)
print(f'\033[1;34mAnalisado o numero {numero}')
sleep(1)
print(f'\033[0;31mUnidade: {num // 1 % 10}')
print(f'\033[32mDezena: {num // 10 % 10}')
print(f'\033[33mCenteza: {num // 100 % 10}')
print(f'\033[36mMilhar: {num // 1000 % 10}')
