def arqExiste(arq):
    try:
         a = open(arq, 'rt')
         a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def arqCria(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('ERRO! na criação do arquivo')
    else:
        print(f'Arquivo \"{arq}\" criado!')

def lerDados(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('ERRO! ao ler o arquivo!')
    else:
        a = a.readlines()
        for p in a:
            pessoa = p.split(';')
            pessoa[1] = pessoa[1].replace('\n', '')
            print(f'{pessoa[0]:<42}{pessoa[1]} Anos')

def addDados(arq):
    try:
        a = open(arq, 'at')
    except:
        print('ERRO! ao tentar adicionar dados')
    else:
        nome = str(input('Nome: ')).strip().title()
        idade = int(input('Idade: '))
        a.write(f'{nome};{idade};\n')
        print(f'Novo registro de {nome} adicionado!')
        a.close()