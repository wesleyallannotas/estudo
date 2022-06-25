def leiaInt(msg):
    n = input(msg).strip()
    while not n.isnumeric():
        print('\033[1;31m', 'ERRO! Digite um numero inteiro valido.', '\033[m', sep='')
        n = input(msg).strip()
    return int(n)


print('-'*30)
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')