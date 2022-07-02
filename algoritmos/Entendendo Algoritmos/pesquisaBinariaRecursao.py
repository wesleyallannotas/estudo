cont = 0
def pesquisaBinaria(lista, val):
    global cont
    cont += 1
    tam = len(lista)
    meio = tam // 2
    if val == lista[meio]:
        return print(lista[meio]) 
    else:
        if val < lista[meio]:
            pesquisaBinaria(lista[:meio], val)
        else:
            pesquisaBinaria(lista[meio:], val)


numeros = [0, 3, 5, 7, 9, 11, 14, 16, 17, 19]
print(f'Lista: {numeros}')
val = int(input('Informe o numero a ser pesquisa: '))
if val in numeros:
    pesquisaBinaria(numeros, val)
    print(cont)
else:
    print('Valor nao pertence a lista!')
    print(cont)
