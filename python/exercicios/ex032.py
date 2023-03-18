from datetime import date

ano = int(input('\033[33mQue ano quer analisar? Coloque 0 para analisar o ano atual: \033[m'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} e \033[1;32mBISSEXTO\033[m')
else:
    print(f'O ano {ano} \033[1;31mNAO e BISSEXTO\033[m')