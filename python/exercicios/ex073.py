brasileirao = ('Palmeiras', 'Corinthians', 'Sao Paulo', 'Internacional',
               'Athetico-PR', 'Atletico-MG', 'Coritiba', 'Fluminense', 
               'Ameria-MG', 'Avai', 'Santos', 'Bragantino', 'Ceara', 'Goias', 
               'Atletico-GO', 'Flamengo', 'Botafogo', 'Cuiaba', 'Juventude', 
               'Fortaleza')
print(f'Lista do times do Brasileirao: {brasileirao}')
print(f'Os 5 primeiros sao {brasileirao[:5]}')
print(f'Os 4 ultimos sao {brasileirao[-4:]}')
print(f'Times em ordem alfabetica: {sorted(brasileirao)}')
print(f'O Santos esta na {brasileirao.index("Santos") + 1} posicao')
