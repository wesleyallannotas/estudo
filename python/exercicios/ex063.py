# Logica aux
'''
print(f'{" Sequencia de Fibonacci ":-^36}')
qunt = int(input('Quantos termos voce quer mostras? '))
cont = pos = 1
ant = 0
print(ant, end=' ➙ ')    
while cont < qunt:
    print(pos, end=' ➙ ')
    aux = ant
    ant = pos
    pos += aux
    cont += 1
print('FIM')
'''

# Logica valores
print(f'{" Sequencia de Fibonacci ":-^36}')
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
cont = 3
print(t1, end=' ➙ ')
print(t2, end=' ➙ ')
while cont <= n:
    t3 = t1 + t2
    print(t3, end=' ➙ ')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
