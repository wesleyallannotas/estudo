jogador = dict()
# total = 0
jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
qnt = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
jogador['gols'] = list()
jogador['total'] = 0
for c in range(0, qnt):
    jogador['gols'].append(int(input(f' Quantos gols na partida {c}? ')))
#     jogador['total'] += jogador['gols'][c]
jogador['total'] = sum(jogador['gols'])
# for g in jogador['gols']:
#     total += g
# jogador['total'] = total
print('-='*23)
print(jogador)
print('-='*23)
for k, v in jogador.items():
    print(f'O compo {k} tem o valor {v}')
print('-='*23)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')