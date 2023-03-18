valores = list()
pares = list()
impares = list()
while True:
    valor = int(input('Digite um numero: '))
    valores.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*35)
print(f'A lista completa {valores}')
print(f'A lista de pares {pares}')
print(f'A lista de impares {impares}')
