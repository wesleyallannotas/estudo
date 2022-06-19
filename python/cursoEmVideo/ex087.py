matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somPar = somTer = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor [{l}, {c}]: '))
print('-='*35)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            somPar += matriz[l][c]
    print()
print('-='*35)
print(f'A soma dos valores pares e {somPar}')
for l in range(0, 3):
    somTer += matriz[l][2]
print(f'A soma dos valores da terceira coluna e {somTer}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif maior < matriz[1][c]:
        maior = matriz[1][c]
print(f'O maior valor da segunda linha e {maior}')
