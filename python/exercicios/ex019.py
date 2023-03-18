from random import choice, randint

aluno1 = input('\033[1;33mPrimeiro Aluno: ')
aluno2 = input('Segunddo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

# Metodo 1
escolhido = choice(alunos)
print(f'\033[mO aluno escolhido foi \033[1;32m{escolhido}\033[m')

# Metodo 2
escolhido = randint(0, 3)
print(f'O aluno escolhido foi {alunos[escolhido]}')
