def metade(num=0):
    return num/2

def dobro(num=0):
    return num*2

def aumento(num=0, por=0):
    return num + (num * por/100)

def moeda(num=0, moeda='R$'):
    return f'{moeda}{num:.2f}'.replace('.', ',')