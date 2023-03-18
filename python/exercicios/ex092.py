from datetime import date
pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - nascimento
pessoa['ctps'] = int(input('Carteira de Trabalho (0 nao tem): '))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salario: R$'))
    contAtual = date.today().year - pessoa['contratação']
    contFalta = 35 - contAtual
    pessoa['aposentadoria'] = pessoa['idade'] + contFalta
print('-='*15)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')