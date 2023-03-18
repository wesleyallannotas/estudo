from random import randint
from time import sleep
print('''Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('Qual e a sua jogada? '))
pc = randint(0, 2)
print('\033[1;31mJO')
sleep(1)
print('\033[1;33mKEN')
sleep(1)
print('\033[1;32mPO!!!\033[1;36m')
resultado = ''
if 0 <= opcao <= 2:
    if opcao == 0:
        opcao = 'PEDRA'
        if pc == 0:
            pc = 'PEDRA'
            resultado = 'EMPATE'
        elif pc == 1:
            pc = 'PAPEL'
            resultado = 'COMPUTADOR VENCE'
        else:
            pc = 'TESOURA'
            resultado = 'JOGADOR VENCE'
    if opcao == 1:
        opcao = 'PAPEL'
        if pc == 0:
            pc = 'PEDRA'
            resultado = 'JOGADOR VENCE'
        elif pc == 1:
            pc = 'PAPEL'
            resultado = 'EMPATE'
        else:
            pc = 'TESOURA'
            resultado = 'COMPUTADOR VENCE'
    if opcao == 2:
        opcao = 'TESOURA'
        if pc == 0:
            pc = 'PEDRA'
            resultado = 'COMPUTADOR VENCE'
        elif pc == 1:
            pc = 'PAPEL'
            resultado = 'JOGADOR VENCE'
        else:
            pc = 'TESOURA'
            resultado = 'EMPATE'
    print('-='*10)
    print(f'''Computador jogou {pc}
Jogador jogou {opcao}''')
    print('-='*10)
    print(resultado)
else:
    print('Opcao Invalidade, tente novamente!')

# Lista
"""
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opcoes:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opcao = int(input('Qual e a sua jogada? '))
print('\033[1;31mJO')
sleep(1)
print('\033[1;33mKEN')
sleep(1)
print('\033[1;32mPO!!!\033[1;36m')
print('-='*10)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[opcao]}')
print('-='*10)
if pc == 0:
    if opcao == 0:
        print('EMPATE')
    elif opcao == 1:
        print('JOGADOR VENCE')
    elif opcao == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVALIDA!')
elif pc == 1:
    if opcao == 0:
        print('JOGADOR VENCE')
    elif opcao == 1:
        print('EMPATE')
    elif opcao == 2:
        print('COMPUTADOR VENCE')
    else:
        print('\033[1;31mJOGADA INVALIDA!')

elif pc == 2:
    if opcao == 0:
        print('COMPUTADOR VENCE')
    elif opcao == 1:
        print('JOGADOR VENCE')
    elif opcao == 2:
        print('EMPATE')
    else:
        print('\033[1;31mJOGADA INVALIDA!')
"""
