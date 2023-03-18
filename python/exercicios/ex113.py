cor = {'red':'\033[1;31m', 'clear':'\033[m'}
def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print(cor['red'], 'ERRO! por favor, digite um numero inteiro valido', cor['clear'], sep='')
            continue
        except KeyboardInterrupt:
            print(cor['red'], '\nEntrada de dados interrompida!', cor['clear'], sep='')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print(cor['red'], 'ERRO! por favor, digite um numero real valido', cor['clear'], sep='')
            continue
        except KeyboardInterrupt:
            print(cor['red'], '\nEntrada de dados interrompida!', cor['clear'], sep='')
            return 0
        else:
            return num


# Programa Principal
numInt = leiaInt('Digite um numero Inteiro: ')
numReal = leiaFloat('Digite um numero Real: ')
print(f'O numero Inteiro foi {numInt} o Real foi {numReal}')