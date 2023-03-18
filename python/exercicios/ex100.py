from random import randint
from time import sleep

def sorteio(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        lst.append(randint(1, 10))
        print(lst[c], end=' ', flush=True)
        sleep(0.3)
    print('PRONTO!')

def somaPar(lst):
    soma = 0
    for c in lst:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {lst}, temos {soma}')


numeros = list()
sorteio(numeros)
somaPar(numeros)
