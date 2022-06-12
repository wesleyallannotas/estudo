from datetime import date
nascimento = int(input('Ano de nascimento: '))
alistamento = nascimento + 18
idade = date.today().year - nascimento
print(f'Quem nasceu em {nascimento} tem {idade} em {date.today().year}')
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o alistamento')
    print(f'Seu alistamento sera em \033[1;32m{alistamento}.\033[m')
elif idade > 18:
    print(f'Voce ja deveria ter se alistado ha {idade - 18} anos')
    print(f'Seu alistamento foi em \033[1;31m{alistamento}.\033[m')
else:
    print('Voce tem que alistar \033[1;31mIMEDIATAMENTO\033[m')
