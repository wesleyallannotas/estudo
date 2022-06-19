pessoas = list()
pes = dict()
soma = media = 0
while True:
    pes.clear()
    pes['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pes['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pes['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F')
    pes['idade'] = int(input('Idade: '))
    pessoas.append(pes.copy())
    soma += pes['idade']
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N') 
    if resp == 'N': # ou in
        break
print('-='*25)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
media = soma / len(pessoas)
print(f'B) A media de idade e de {media:5.2f} anos')
print('C) As mulheres cadastradas foram ', end='')
for pes in pessoas:
    if pes['sexo'] == 'F': # ou in
        print(pes['nome'], end=', ')
print()
print('D) Lista das pessoas que estão acima da media:')
for i in pessoas:
    if i['idade'] > media:
        for k, v in i.items():
            print(f'  {k} = {v};', end='')
        print()
print('<<< ENCERRADO >>>')