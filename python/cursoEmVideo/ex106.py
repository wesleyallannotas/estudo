cor = {'red':'\033[1;31m', 'blue':'\033[1;36m', 'green':'\033[1;32m', 'clear':'\033[m'}

def titulo(msg, cores=cor['blue']):
    tam = len(msg) + 4
    print(cores)
    print('~'*tam, f'  {msg}  ', '~'*tam, sep='\n')
    print(cor['clear'])

def ajuda():
    from time import sleep
    while True:
        titulo("SISTEMA DE AJUDA PyHELP")
        fun = str(input('Função ou Biblioteca (\'fim\' encerra) >>> ')).strip()
        if fun == 'fim':
            titulo('OBRIGADO! Volte sempre', cor['green'])
            break
        titulo(f'Acessando o manual do comando \'{fun}\'', cor['red'])
        sleep(0.5)
        print(cor['green'])
        help(fun)


ajuda()