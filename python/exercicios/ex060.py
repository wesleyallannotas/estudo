# Loop While
''''
num = int(input('Digite um numero para calcular sua fatorial: '))
print(f'Calculando {num}!', end=' = ')
fatorial = 1
while num > 0:
    print(num, end='')
    print(' X ' if num > 1 else ' = ', end='')
    fatorial *= num
    num -= 1
print(fatorial)
'''

# Modulo 
'''
from math import fatorial
n = int(input('Digite um numero para calcular seu fatorial: '))
f = factorial(n)
print('O factorial de {n}! e {f}')
'''

# Loop For
num = int(input('Digite um numero para calcular sua fatorial: '))
print(f'Calculando {num}!', end=' = ')
fatorial = 1
for c in range(num, 0, -1):
    print(num, end='')
    print(' X ' if c > 1 else ' = ', end='')
    fatorial *= c
print(fatorial)
