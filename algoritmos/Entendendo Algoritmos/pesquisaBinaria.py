def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None


numeros = [0, 3, 5, 7, 9, 11, 14, 16, 17, 19]
numPes = int(input('Numero a se pesquisado: '))

if pesquisa_binaria(numeros, numPes) == None:
    print(f'O numero {numPes} nao pertence a lista')
else:
    print(f'O numero {numPes} se encontra na posição {pesquisa_binaria(numeros, numPes)}')