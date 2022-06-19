valores = list()
while True:
    resp = ' '
    valores.append(int(input('Digite um valor: ')))
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*35)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente sao {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 nao faz parte da lista!')
