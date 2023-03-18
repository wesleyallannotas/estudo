aluno = dict()
aluno['nome'] = str(input('Nome: ')).title()
aluno['media'] = float(input(f'Media de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['status'] = 'Aprovado'
elif aluno['media'] < 5:
    aluno['status'] = 'Reprovado'
else:
    aluno['status'] = 'Recuperação'
print('-='*40)
for k, v in aluno.items():
    print(f' - O {k} e igual a {v}')