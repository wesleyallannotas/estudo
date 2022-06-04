from random import shuffle

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('A ordem de apresentacao sera:', end=' = ')
print(alunos)
