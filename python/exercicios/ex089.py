alunos = list()
aln = 0
while True:
    nome = str(input('Nome: ')).strip().title()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    med = (n1 + n2) / 2
    alunos.append([nome, [n1, n2], med])
    resp = ' ' 
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*40)
print(f'{"No.":<5}', f'{"NOME":<20}', f'{"MEDIA":<10}')
print('-'*35)
for i, aluno in enumerate(alunos):
    print(f'{i:<5}', f'{aluno[0]:<20}', f'{aluno[2]:<10.1f}')
print('-'*40)
while True:
    aln = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aln == 999:
        print('FINALIZANDO...')
        break
    elif aln <= len(alunos) - 1:
        print(f'Notas de {alunos[aln][0]} sao {alunos[aln][1]}')
print('<<< Volte Sempre >>>')