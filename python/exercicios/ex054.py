from datetime import date
maiores = 0
menores = 0
for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c} pessoa nasceu? '))
    if date.today().year - nascimento >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Ao todo timvemos {maiores} pessoas maiores de idade')
print(f'E tambem tivemos {menores} pessoas menores de idade')
