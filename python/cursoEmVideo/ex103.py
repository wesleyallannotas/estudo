def ficha(nome='<desconhecido>', gols=0): 
    if not nome.strip().isalpha():
        nome='<desconhecido>'
    if not gols.strip().isnumeric():
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato')


print('-'*30)
ficha(input('Nome do Jogador: '), input('Numero de Gols: '))