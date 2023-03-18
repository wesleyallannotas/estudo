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

def moeda(num=0, moeda='R$',):
    return f'{moeda}{num:.2f}'.replace('.', ',')