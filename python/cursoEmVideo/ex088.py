from random import randint
from time import sleep
matriz = [] # list()
print('-'*35)
print(f'{"JOGA NA MEGA SENA":^35}')
print('-'*35)
qnt = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-='*3, f'{f"SORTEANDO {qnt} JOGOS":^20}', '-='*3)
for l in range(0, qnt):
    matriz.append([])   # list()
    for c in range(0, 5):
        val = randint(1, 61)
        while val in matriz[l]:
            val = randint(1, 61)
        matriz[l].append(val)
    matriz[l].sort()
for p, l in enumerate(matriz):
    print(f'Jogo {p+1:>2}: {l}')
    sleep(0.5)
print('-='*3, f'{"< BOA SORTE! >":^7}', '-='*3)