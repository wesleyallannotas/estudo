from random import randint
yellow = '\033[33m'
blue = '\033[1;36m'
green = '\033[1;32m'
red = '\033[1;31m'
clear = '\033[m'
cont = 0
print(yellow, '=-'*20, clear)
print(blue, f"{'VAMOS JOGAR PAR OU IMPAR':^40}", clear)
print(yellow, '=-'*20, clear)
while True:
    pcVal = randint(1, 10)
    jogVal = int(input('Dige um valor: '))
    somaVal = pcVal + jogVal
    jogDes = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    while jogDes not in 'PI':
        jogDes = str(input(f'{red}Invalido, Tente novamente...{clear} Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jogVal} e o computador {pcVal}. Total de {somaVal}', end=' ')
    print('DEU PAR' if somaVal % 2 == 0 else 'DEU IMPAR')
    if jogDes == 'P':
        if somaVal % 2 == 0: 
            print(f'Voce {green}VENCEU!', clear)
            print('Vamos jogar novamente...')
        else:
            print(f'Voce {red}PERDEU!', clear)
            break
    else:
        if somaVal % 2 != 0: 
            print(f'Voce {green}VENCEU!', clear)
            print('Vamos jogar novamente...')
        else:
            print(f'Voce {red}PERDEU!', clear)
            break
    cont += 1
    print(yellow, '=-'*20, clear)
print(f'{red}GAME OVER!{clear} Voce ganho {blue}{cont}{clear} vezes')
