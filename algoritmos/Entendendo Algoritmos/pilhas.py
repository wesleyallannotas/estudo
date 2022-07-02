def sauda(nome):
    print(f'Ola, {nome}!')
    sauda2(nome)
    print('Preparando para dizer tchau...')
    tchau()

def sauda2(nome):
    print(f'Como vai {nome}?')

def tchau():
    print('Ok, Tchau!')

sauda('Wesley')
