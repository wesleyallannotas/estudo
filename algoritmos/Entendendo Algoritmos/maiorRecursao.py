# Meu algoritmo
def maiorLista(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    else:
        if lista[0] <= lista[1]:
            return maiorLista(lista[1:])
        else:
            lista.pop(1)
            return maiorLista(lista)

# Algoritmo Livro
def maximoLista(lista):
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    sub_max = maximoLista(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max


lista = [1, 4, 2, 4, 8 , 0, 85, 33, 18, 23, 75]
print(maiorLista(lista))
print(maximoLista(lista))
