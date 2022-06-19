time = list()
jogador = dict()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().title()
    jogador['gols'] = list()
    qnt = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(1, qnt+1):
        jogador['gols'].append(int(input(f'Quantos gols na partida {p}? ')))
    jogador['total'] = sum(jogador['gols'])
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda com S ou N')
    if resp == 'N':
        break
print('-='*20)
# Cabeçalho
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
# Preenchendo tabela
for i, j in enumerate(time):
#     print(f'{i:>3}', f'{j["nome"]:<15}', f'{str(j["gols"]):<15}', f'{j["total"]:<7}')
    print(f'{i:>4}', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*20)
while True:
    jogador = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if jogador == 999:
        break
    elif jogador >= len(time) or jogador < 0:
        print(f'ERRO! Nao existe jogador com código {jogador}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[jogador]["nome"]}:')
        for i, j in enumerate(time[jogador]['gols']):
            print(f'No jogo {i+1} fez {j} gols.')
print('<<< ENCERRAMENTO >>>')