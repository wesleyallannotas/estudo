# Cada função possui uma forma de criar o if
def metade(num=0, formato=False):
    res = num / 2
    return res if format == False else moeda(res)

def dobro(num=0, formato=False):
    res = num * 2
    return num if format is False else moeda(res)

def aumento(num=0, por=0, formato=False):
    res = num + num * por / 100
    return res if not format else moeda(res)

def reducao(num=0, por=0, formato=False):
    res = num - num * por / 100
    return res if not format else moeda(res)

def moeda(num=0, moeda='R$',):
    return f'{moeda}{num:.2f}'.replace('.', ',')

def resumo(num=0, aumPor=0, redPor=0):
    print('-'*35, f'{"RESUMO DO VALOR":^35}', '-'*35, sep='\n')
    print(f'{"Preço analisado:":<25}', f'{moeda(num):<}', sep='')
    print(f'{"Dobro do preço:":<25}', f'{dobro(num, True):<}', sep='')
    print(f'{"Metade do preço:":<25}', f'{metade(num, True):<}', sep='')
    print(f'{f"{aumPor}% de aumento:":<25}', f'{aumento(num, aumPor, True):<}', sep='')
    print(f'{f"{redPor}% de redução:":<25}', f'{reducao(num, redPor, True):<}', sep='')