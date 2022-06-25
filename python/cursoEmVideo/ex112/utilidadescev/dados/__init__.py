def leiaDinheiro(msg):
    while True:
        num = str(input(msg)).strip().replace(',', '.')
        try:
            return float(num)
        except:
            print('\033[1;31m', f'ERRO: \"{num}\" e um preço invalido!', '\033[m', sep='')

def leiaDinheirocv(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).strip().replace(',', '.')
        if entrada.isalpha() or entrada == '':
            print('\033[1;31m', f'ERRO: \"{entrada}\" e um preço invalido!', '\033[m', sep='')
        else:
            valido = True
            return float(entrada)