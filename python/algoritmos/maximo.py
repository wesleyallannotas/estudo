def maximo(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximo(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max


lista = [1, 2, 3, 13, 77, 23, 43, 64]
print(maximo(lista))
