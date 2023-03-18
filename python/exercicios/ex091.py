from random import randint
from time import sleep
from operator import itemgetter
cont = 0
jogadores = dict()
for c in range(0, 4):
    jogadores[f'jogador{c}'] = randint(1, 6)
#    print(f'jogador{c} tirou {jogadores[f"jogador{c}"]} no dado.')
#    sleep(0.3)

# for apenas para imprimir dados
for k, v in jogadores.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.3)

print('-='*40)
print('=== RANKING DOS JOGADORES ===')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) # itemgetter(0) seleciona a chave, itemgetter(1) seleciona o valor
# ranking sera uma lista com tuplas dentro
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}')