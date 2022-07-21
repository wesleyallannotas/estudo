# Função recursiva com pilha de chamadas
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)


cor = {'red':'\033[1;31m', 'green':'\033[1;32m', 'blue':'\033[1;36m', 'clear':'\033[m'}
while True:
    try:
        num = int(input(f'{cor["blue"]}Informe um numero inteiro para receber seu fatorial: '))
    except KeyboardInterrupt:
        print(cor['red'], 'Encerrando...', cor['clear'])
        break
    except:
        print(cor['red'], 'ERRO! Tente novamente..', cor['clear'])
        continue
    else:
        print(cor['green'], f'O fatorial de {num} e {fat(num)}', cor['clear'])
        break