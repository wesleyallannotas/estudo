pessoas = list()   # pessoas = []
pessoa = list()    # pessoa = []
menor = maior = 0
while True:
    pessoa.append(str(input('Nome: ')).strip().title())
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = pessoa[1]
    else:
        if maior < pessoa[1]:
            maior = pessoa[1]
        if menor > pessoa[1]:
            menor = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*35)
print(f'Ao todo, voce cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(pessoa[0], end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(pessoa[0], end=' ')