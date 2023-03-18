quantidadeMulherNova = 0
idadeSoma = 0
idadeHomemVelho = 0
nomeHomemVelho = ''
for c in range(1, 5):
    print('\033[1;33m-='*6 + f'\033[1;36m {c} PESSOA ' + '\033[1;33m=-\033[m'*6)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    idadeSoma += idade
    if sexo[0] in 'Mm' and idade > idadeHomemVelho: # if sexo in 'Mm':
        nomeHomemVelho = nome
        idadeHomemVelho = idade
    elif sexo[0] in 'Ff' and idade < 20: # if sexo in 'Ff'
        quantidadeMulherNova += 1
print('\033[1;31m-'*6 + ' RESULTADO ' + '-'*6)
idadeMedia = idadeSoma / 4
print(f'\033[mA media de idade do grupo e de {idadeMedia} anos')
print(f'O homem mais velho tem {idadeHomemVelho} anos e se chama {nomeHomemVelho.title()}')
print(f'Ao todo sao {quantidadeMulherNova} mulheres com menos de 20 anos')
