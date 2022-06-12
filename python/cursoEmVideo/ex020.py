from random import shuffle

aluno1 = input('\033[1;31;47mPrimeiro Aluno: ')
aluno2 = input('\033[1;32;44mSegundo Aluno: ')
aluno3 = input('\033[1;36;42mTerceiro Aluno: ')
aluno4 = input('\033[1;35;46mQuarto Aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(alunos)
print('\033[1;7;40mA ordem de apresentação sera:', end=' = ')
print(alunos)
