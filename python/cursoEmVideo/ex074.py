from random import randint
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), 
           randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in sorteio:
    print(n, end=' ')

# Usando sorted() e fatiamento
print(f'\nO maior valor sorteado foi {sorted(sorteio)[-1]}')
print(f'O menor valor sorteado foi {sorted(sorteio)[0]}')
# mex() e min()
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')
