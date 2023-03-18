red = '\033[1;31m'
clear = '\033[m'
contMais= contMul = contMasc = 0
while True:
    print('='*35)
    print(f'{"CADASTRE UM PESSOA":^35}')
    print('='*35)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input(f'{red}Invalido, Tente novamente...{clear} Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        contMais+= 1
    if sexo == 'M':
        contMasc += 1
    if idade < 20 and sexo == 'F':
        contMul += 1
    continuar = str(input('Quer Continuar: [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input(f'{red}Invalido, Tente novamente...{clear} Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('='*35)
print(f'Total de pessoas com mais de 18 anos: {contMais}')
print(f'Ao todo temos {contMasc} homens cadastrados')
print(f'E temos {contMul} mulheres com menos de 20 anos')
