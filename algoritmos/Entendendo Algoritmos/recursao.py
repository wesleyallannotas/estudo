def regressiva(i):
    print(i)
    if i <= 1:  # Caso-Base
        return
    else:       # Caso Recursivo
        regressiva(i-1)


while True:
    i = int(input('Informe um numero para contagem regressiva: '))
    if i > 0:
        regressiva(i)
        break
    else:
        i = int(input('ERRO! informe um numero maior que 0: '))
