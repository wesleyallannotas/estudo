from random import choice, randint

aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segunddo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

# Metodo 1
escolhido = choice(alunos)
print(f'O aluno escolhido foi {escolhido}')

# Metodo 2
escolhido = randint(0, 3)
print(f'O aluno escolhido foi {alunos[escolhido]}')
