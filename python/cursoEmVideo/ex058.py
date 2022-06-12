from random import randint
pc = randint(1, 10)
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegui adivinhar qual foi?')
jogador = 0
while pc != jogador:
    jogador = int(input('Qual e seu palpite? '))
    if jogador < pc:
        print('Mais... Tenta mais uma vez.')
    elif jogador > pc:
        print('Menos... Tente mais uma vez.')
print('Acertou!')

# Boolean
'''
from random import randint
pc = randint(1, 10)
print('Sou seu computador...\nAcabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegui adivinhar qual foi?')
acertou = False
while not acertou:
    jogador = int(input('Qual e seu palpite? '))
    if jogador == pc:
        acertou = True
    elif jogador > pc:
        print('Menos... Tente novamente')
    else:
        print('Mais... Tente novamente')
print('Acertou!')
'''
